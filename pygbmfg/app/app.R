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

yield_tbl <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "v_gb_yield"))
lineage_tbl <- dplyr::tbl(con, dbplyr::in_schema("gbmfg", "v_gb_lineage"))
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
####
ui <- dashboardPage(
    dashboardHeader(title = "Gel Bead Manufacturing"),
    dashboardSidebar(
        sidebarMenu(
            menuItem("Yield", tabName = "yield", icon = icon("dashboard")),
            menuItem("Genealogy", tabName = "gene", icon = icon("project-diagram"))
            #menuItem("Spec Details", tabName = "spec_detail", icon = icon("check-square")),
            #menuItem("Spec Summary", tabName = "spec_summary", icon = icon("check-square"))
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
                                    choices = c("2000058", "210170"))
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
            )
        )
    )
)

server <- function(input, output, session) {
  
  output$yield_trend <- renderPlotly({
    yield_tbl %>% 
      mutate(yield = gb_vol_for_dispense/unfunc_vol*100) %>% 
      dplyr::filter(pn == local(input$pn)) %>% 
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
      dplyr::filter(pn == local(input$pn)) %>% 
      ggplot(.,aes(x = step, y = qty, color = ln)) +
      geom_line(aes(group = ln)) +
      scale_color_brewer(palette="Set1") +
      theme_classic() +
      labs(y = "Volume of GBs (mL)", y = "Step") +
      theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
  })
  
  output$mat_loss <- renderPlotly({
    vols %>% 
      dplyr::filter(pn == local(input$pn)) %>% 
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
}

shinyApp(ui, server)

