# Blazer Styling

## Question

**WOL** asked on 28 Dec 2020

What is it that I'm missing when I have a Blazer Telerik Grid specified this way on a razor page: @page "/households" <h3>Households</h3> <TelerikGrid Data="Model" Height="550px" Sortable="true"> <GridColumns> <GridColumn Field="Name" Title="Name" /> <GridColumn Field="Lies_District" Title="District" /> <GridColumn Field="Openings" Title="Openings" /> <GridColumn Field="EmailAddress" Title="Email" /> <GridColumn Field="JoinedOn_DateTime" Title="JoinedOn" /> <GridColumn Field="ReportCount" Title="Reports" /> <GridColumn Field="LastReport" Title="Last Report" /> </GridColumns> </TelerikGrid> and the resulting page has no grid lines, headings all smashed together with only one space between title columns?

## Answer

**Marin Bratanov** answered on 28 Dec 2020

Hi Wolfgang, You need to make sure that you also have the necessary assets such as styles for our components, this article explains them in detail: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need.) If you are using our Blazor component on a Razor page and not in a Blazor app, I'd also recommend you review the information and readme files in those sample projects too: [https://github.com/telerik/blazor-ui/tree/master/common/razor-components.](https://github.com/telerik/blazor-ui/tree/master/common/razor-components.) Regards, Marin Bratanov
