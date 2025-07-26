# Toolbar css difference

## Question

**WimWim** asked on 21 Jan 2021

Hello Since the latest version float-right is no longer working in the ToolBar of the Grid and the ToolBar disappears sometimes. The disappearance if the Grid does not happen with <link href="_content/Telerik.UI.for.Blazor/css/kendo-theme-bootstrap/all.css" rel="stylesheet" /> but the float-right does not work. When I use the Sass Theme builder, there are differences in the css and the ToolBar disappears sometimes. For example the standard bootstrap css has: .k-grid-toolbar { border-width: 0 0 1px; -ms-flex-negative: 0; flex-shrink: 0; } And the generated css has this but is not set on the toolbar: .k-toolbar> * { -ms-flex-negative: 0; flex-shrink: 0; display: -ms-inline-flexbox; display: inline-flex; -ms-flex-align: stretch; align-items: stretch; -ms-flex-line-pack: center; align-content: center; vertical-align: middle } Is the generated css updated to the latest version and why does the float-right not work?

## Answer

**Svetoslav Dimitrov** answered on 21 Jan 2021

Hello Wim, As part of our 2.21.0 release, we have made an enhancement for the SearchBox where it can be positioned to the left as well. The default value in the CSS is to place it to the left side so we have updated the documentation and the demo to show how to place it back to the right-hand side. Code snippet: <GridToolBar> <span class="k-toolbar-spacer"> </span> @* add this spacer to keep the searchbox on the right *@<GridSearchBox /> </GridToolBar> Regards, Svetoslav Dimitrov
