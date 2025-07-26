# Embed chart in spreadsheet

## Question

**mic** asked on 16 Dec 2020

We have a Blazor server app that has a dashboad type layout. What we'd like to do is export the charts and the data behind from the dashboard to the an Excel spreadsheet for download. Generating the dashbard, charts and spreadsheet looks straight forward with your components. The part I'm struggling with is how to embed the charts from the dashboard into the spreadsheet. Is this supported?

## Answer

**Marin Bratanov** answered on 16 Dec 2020

Hello Michael, A dashboard is easy to make with our components, we have several examples ( sample app, a project template, the TileLayout demos ). Exporting that to Excel is the challenge - the end result of the components is HTML, and you can't convert that to Excel, Excel needs tabular data only. Moreover, in Blazor there is no provision to get rendering or templates to even attempt to put that rendering in excel. Thus, what I can suggest is that you consider the following: Build your own backend that will generate the required excel file in a fashion similar to this sample project. Pass necessary information from the Blazor app to it (such as the tilelayout state, grid DataSourceRequest objects, anything else you need to build the custom spreadsheet). Consider making it a .NET "Classic" backend so you can add charts to it, or if they are not urgent - Follow this feature request for the ability to add charts in .netstarndard. Regards, Marin Bratanov
