# Can I use a ComboBox in the FilterRow

## Question

**dca** asked on 18 Feb 2020

I am remotely retrieving my paged data that is displayed in my Telerik Blazor UI Grid from an OData ASP.NET Core 3.1 web API I have several fields that are enums in each of my records. I would like to have the columns that have enum based properties display a combobox in the FilterRow so I can select from the desired enum options to filter my grid. For example, My OData API metadata shows the enum values as; <p> <Property Name="AccountType" Type="API.Server.Enums.AccountTypes" Nullable="false" /></p><p></p> And so when I query the API using Postman, I need to use the string . <p>..?$filter=AccountType eq EII.CDAPI.Server.Enums.AccountTypes'Customer' </p><p></p> So, I assume that the filter you would generate from a FilterRow ComboBox selection would have similar syntax. Is this possible?

## Answer

**Marin Bratanov** answered on 19 Feb 2020

Hello, You can Follow the implementation of enum filteres in the grid in this page (I added your Vote for you): [https://feedback.telerik.com/blazor/1443614-filter-enum-values.](https://feedback.telerik.com/blazor/1443614-filter-enum-values.) It offers a few other relevant features you may want to Vote for and Follow (such as custom filter components), and a conceptual workaround through your own filters outside of the grid. Regards, Marin Bratanov
