.libPaths(new = c("/mnt/home/niranjan.ilawe/R/x86_64-conda_cos6-linux-gnu-library/3.6",
                  "/mnt/opt/R/R-3.6.1-conda-openblas/R-library",
                  "/mnt/opt/R/R-3.6.1-conda-openblas/env/lib/R/library"))

options(shiny.usecairo = FALSE)

library(shiny)
library(shinydashboard)
library(tidyverse)
library(plotly)
library(DT)

#### Connecting to sources #######
con <- DBI::dbConnect(RPostgres::Postgres(),
                      host = "cpdda.c7qfiffzqhfr.us-west-2.rds.amazonaws.com",
                      user = "cpdda",
                      password = ">TKd=lN7>jUiXTK.pSKV")

pn_master <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "pn_master"))

yield_tbl <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "v_gb_yield")) %>% 
  left_join(pn_master, by = c("pn" = "func")) %>% 
  mutate(desc = paste0(desc, " (", pn, ")"))

lineage_tbl <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "v_gb_lineage")) %>% 
  left_join(pn_master, by = c("pn" = "unfunc")) %>% 
  mutate(desc = paste0(desc, " (", pn, ")"))

flowcam_tbl <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "func_flowcam_data")) %>% 
  left_join(pn_master, by = c("pn" = "func")) %>% 
  mutate(desc = paste0(desc, " (", pn, ")"))

divvar_tbl <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "func_divvar_data")) %>% 
  left_join(pn_master, by = c("pn" = "func")) %>% 
  mutate(desc = paste0(desc, " (", pn, ")"))

guava_tbl <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "disp_guava_data")) %>% 
  left_join(pn_master, by = c("pn" = "disp")) %>% 
  mutate(desc = paste0(desc, " (", pn, ")"))

hsv_tbl <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "disp_hsv_data")) %>% 
  left_join(pn_master, by = c("pn" = "disp")) %>% 
  mutate(desc = paste0(desc, " (", pn, ")")) %>% 
  filter(!pn %in% c("1000841", "2000173")) %>% 
  collect() %>% 
  mutate(date1 = lubridate::mdy(qc_date),
         date2 = lubridate::ymd(qc_date),
         qc_date = if_else(is.na(date1), date2, date1))

#### End of connecting to sources ####

#### Color Palette ####
cbPalette <- c("#999999", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")


##### Clean tables ######
vols <- yield_tbl %>% 
  pivot_longer(cols = c(unfunc_vol, 
                        total_lig1_volume, 
                        total_lig2_volume, 
                        func_vol, 
                        #gb_vol_for_packaging, 
                        gb_vol_for_dispense, 
                        mfg_qty, 
                        qty_to_inventory), 
               names_to = "step", values_to = "qty") %>% 
  dplyr::filter(step %in% c("unfunc_vol", 
                            "total_lig1_volume", 
                            "total_lig2_volume", 
                            "func_vol", 
                            "gb_vol_for_packaging",
                            "gb_vol_for_dispense")) %>% 
  collect()

vols$step <- factor(vols$step, levels = c("unfunc_vol", 
                                          "total_lig1_volume", 
                                          "total_lig2_volume", 
                                          "func_vol", 
                                          "gb_vol_for_packaging",
                                          "gb_vol_for_dispense"))
#### UI #####
ui <- dashboardPage(
  dashboardHeader(title = "Gel Bead Manufacturing"),
  dashboardSidebar(
    sidebarMenu(
      menuItem("Yield", tabName = "yield", icon = icon("dashboard")),
      menuItem("Genealogy", tabName = "gene", icon = icon("project-diagram")),
      menuItem("FlowCam QC", tabName = "flowcam", icon = icon("check-square")),
      menuItem("DivVar QC", tabName = "divvar", icon = icon("check-square")),
      menuItem("Guava QC", tabName = "guava", icon = icon("check-square")),
      menuItem("HSV QC", tabName = "hsv", icon = icon("check-square"))
    )
  ),
  dashboardBody(
    tabItems(
      tabItem(tabName = "yield",
              fluidRow(width = NULL,
                       column(width = 2,
                              box(width = NULL,
                                  selectInput("pn", 
                                              "Select GB PN",
                                              choices = c())
                              ),
                       ),
                       column(width = 5,
                              box(width = NULL,
                                  plotlyOutput("yield_trend")
                              )
                       ),
                       column(width = 5,
                              box(width = NULL,
                                  plotlyOutput("step_loss")
                              )
                       )
              ),
              fluidRow(
                column(width = 2
                       
                ),
                column(width = 5,
                       box(width = NULL,
                           plotlyOutput("mat_loss")
                       )
                )
              )
      ),
      tabItem(tabName = "gene",
              fluidRow(
                column(width = 12,
                       box(width = NULL,
                           collapsible = TRUE,
                           div(style = 'overflow-y: scroll', DT::dataTableOutput('lineage_tbl'))
                       )
                )
              )
      ),
      tabItem(tabName = "flowcam",
              fluidRow(
                column(width = 3,
                       box(width = NULL,
                           selectInput("flowcam_pn", "Select PN", choices = c()),
                           selectInput("flowcam_met", "Select Metric", choices = c()),
                           downloadButton("dl_flowcam", "Download All Data")
                       )
                ),
                column(width = 9,
                       box(width = NULL,
                           plotlyOutput("flowcam_trend")
                       )
                )
              )
      ),
      tabItem(tabName = "divvar",
              fluidRow(
                column(width = 3,
                       box(width = NULL,
                           selectInput("divvar_pn", "Select PN", choices = c()),
                           selectInput("divvar_met", "Select Metric", choices = c()),
                           downloadButton("dl_divvar", "Download All Data")
                       )
                ),
                column(width = 9,
                       box(width = NULL,
                           plotlyOutput("divvar_trend")
                       )
                )
              )
      ),
      tabItem(tabName = "guava",
              fluidRow(
                column(width = 3,
                       box(width = NULL,
                           selectInput("guava_pn", "Select PN", choices = c()),
                           selectInput("guava_met", "Select Metric", choices = c("gb_conc", "pbeads")),
                           downloadButton("dl_guava", "Download All Data")
                       )
                ),
                column(width = 9,
                       box(width = NULL,
                           plotlyOutput("guava_trend")
                       )
                )
              )
      ),
      tabItem(tabName = "hsv",
              fluidRow(
                column(width = 3,
                       box(width = NULL,
                           selectInput("hsv_pn", "Select PN", choices = c()),
                           selectInput("hsv_met", "Select Metric", choices = c("ggf", "bif", "n_equal_0", "n_equal_1", "n_greater_1", "cg_rate", "tether_rate", "drift")),
                           selectInput("hsv_x_axis", "Select X Axis", choices = c("qc_date", "wo")),
                           selectInput("hsv_color", "Select Color By", choices = c("chip_lot", "oil_lot", "bead_lot", "novec_lot", "plateau_ht")),
                           downloadButton("dl_hsv", "Download All Data")
                       )
                ),
                column(width = 9,
                       box(width = NULL,
                           plotlyOutput("hsv_trend")
                       )
                )
              )
      )
    )
  )
)

##### SERVER #####
server <- function(input, output, session) {
  
  observe({
    yield_pns <- yield_tbl %>% distinct(desc) %>% pull(desc)
    updateSelectInput(inputId = "pn",
                      choices = yield_pns)
  })
  
  output$yield_trend <- renderPlotly({
    yield_tbl %>% 
      mutate(yield = gb_vol_for_dispense/unfunc_vol*100) %>% 
      dplyr::filter(desc == local(input$pn)) %>% 
      select(ln, yield) %>% 
      ggplot(., aes(x = ln, y = yield, group = ln)) +
      geom_line(group = 1) +
      geom_point(size = 2) +
      geom_text(aes(label = glue::glue("{round(yield,0)} %"), vjust = -1)) +
      theme_classic() +
      labs(y = "Yield (Unfunc GBs/Func GBs after wash) %", y = "Lot Number")
  })
  
  output$step_loss <- renderPlotly({
    vols %>% 
      dplyr::filter(desc == local(input$pn)) %>% 
      ggplot(.,aes(x = step, y = qty, color = ln)) +
      geom_line(aes(group = ln)) +
      scale_color_brewer(palette="Set1") +
      theme_classic() +
      labs(y = "Volume of GBs (mL)", y = "Step") +
      theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
  })
  
  output$mat_loss <- renderPlotly({
    vols %>% 
      dplyr::filter(desc == local(input$pn)) %>% 
      ggplot(.,aes(x = ln, y = qty, color = step)) +
      geom_line(aes(group = step)) +
      scale_color_manual(values = cbPalette) +
      theme_classic() +
      theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
  })
  
  lineage_df <- reactive({lineage_tbl %>% collect()})
  
  output$lineage_tbl <- renderDT(lineage_df(), filter = 'top', extensions = 'Buttons', selection = 'single', options = list(
    autoWidth = TRUE,
    dom = 'Bfrtip',
    buttons = c('copy', 'csv', 'excel', 'pdf', 'print')))
  
  #### Flowcam ------------
  observe({
    flowcam_pns <- flowcam_tbl %>% distinct(desc) %>% pull(desc)
    updateSelectInput(inputId = "flowcam_pn",
                      choices = flowcam_pns)
  })
  
  observe({
    sel_pn <- input$flowcam_pn
    metrics <- flowcam_tbl %>% filter(desc == sel_pn) %>% distinct(data_name) %>% pull(data_name)
    updateSelectInput(inputId = "flowcam_met",
                      choices = metrics)
  })
  
  output$flowcam_trend <- renderPlotly({
    flowcam_tbl %>% 
      filter(desc == local(input$flowcam_pn),
             data_name == local(input$flowcam_met)) %>% 
      group_by(ln) %>% 
      mutate(data_avg = mean(data_value, na.rm = TRUE)) %>% 
      ungroup() %>%
      ggplot(., aes(x = reorder(ln, date), y = data_value)) +
      geom_point(color = "red") +
      geom_line(aes(y = data_avg), group = 1) +
      theme_classic() +
      labs(y = input$flowcam_met, x = "Lot Number") +
      theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
  })
  
  output$dl_flowcam <- downloadHandler(
    filename = function() {
      paste("flowcam_", Sys.time(), '.csv', sep='')
    },
    content = function(con) {
      readr::write_csv(flowcam_tbl %>%
                         collect(), con)
    }
  )
  
  #### DivVar ------------
  observe({
    divvar_pns <- divvar_tbl %>% distinct(desc) %>% pull(desc)
    updateSelectInput(inputId = "divvar_pn",
                      choices = divvar_pns)
  })
  
  observe({
    sel_pn <- input$divvar_pn
    metrics <- divvar_tbl %>% filter(desc == sel_pn) %>% distinct(data_name) %>% pull(data_name)
    updateSelectInput(inputId = "divvar_met",
                      choices = metrics)
  })
  
  output$divvar_trend <- renderPlotly({
    divvar_tbl %>% 
      filter(desc == local(input$divvar_pn),
             data_name == local(input$divvar_met)) %>% 
      group_by(ln, family) %>% 
      mutate(data_avg = mean(data_value, na.rm = TRUE)) %>% 
      ungroup() %>%
      ggplot(., aes(x = reorder(ln, date), y = data_value)) +
      geom_point(color = "red") +
      geom_line(aes(y = data_avg), group = 1) +
      theme_classic() +
      labs(y = input$divvar_met, x = "Lot Number") +
      theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
      facet_grid(~family)
  })
  
  output$dl_divvar <- downloadHandler(
    filename = function() {
      paste("divvar_", Sys.time(), '.csv', sep='')
    },
    content = function(con) {
      readr::write_csv(divvar_tbl %>%
                         collect(), con)
    }
  )
  
  #### Guava -----------------
  observe({
    guava_pns <- guava_tbl %>% distinct(desc) %>% pull(desc)
    updateSelectInput(inputId = "guava_pn",
                      choices = guava_pns)
  })
  
  output$guava_trend <- renderPlotly({
    guava_tbl %>% 
      filter(desc == local(input$guava_pn)) %>% 
      group_by(lot) %>% 
      mutate(gb_conc_avg = mean(gb_conc, na.rm = TRUE),
             pbeads_avg = mean(pbeads, na.rm = TRUE)) %>% 
      ungroup() %>% 
      ggplot(., aes_string(x = "reorder(lot, date)", y = input$guava_met)) +
      geom_point(color = "red") +
      geom_line(aes_string(y = paste0(input$guava_met, "_avg")), group = 1) +
      theme_classic() +
      labs(x = "Lot Number") +
      theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
  })
  
  output$dl_guava <- downloadHandler(
    filename = function() {
      paste("guava_", Sys.time(), '.csv', sep='')
    },
    content = function(con) {
      readr::write_csv(guava_tbl %>%
                         collect(), con)
    }
  )
  
  #### HSV -----------------
  observe({
    hsv_pns <- hsv_tbl %>% distinct(desc) %>% pull(desc)
    updateSelectInput(inputId = "hsv_pn",
                      choices = hsv_pns)
  })
  
  output$hsv_trend <- renderPlotly({
    hsv_tbl %>% 
      mutate(data = as.numeric(!!sym(input$hsv_met))) %>% 
      filter(desc == input$hsv_pn) %>%
      ggplot(., aes_string(x = paste0("reorder(",input$hsv_x_axis,",qc_date)"), y = "data", color = input$hsv_color)) +
      geom_jitter() +
      theme_classic() +
      labs(x = input$hsv_x_axis, y = input$hsv_met) +
      theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) 
  })
  
  output$dl_hsv <- downloadHandler(
    filename = function() {
      paste("hsv_", Sys.time(), '.csv', sep='')
    },
    content = function(con) {
      readr::write_csv(hsv_tbl, con)
    }
  )
}

shinyApp(ui, server)

