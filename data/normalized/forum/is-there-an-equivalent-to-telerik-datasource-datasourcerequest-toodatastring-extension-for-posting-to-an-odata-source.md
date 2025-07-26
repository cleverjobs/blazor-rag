# Is there an equivalent to Telerik.DataSource.DataSourceRequest.ToOdataString() extension for posting to an odata source?

## Question

**Jst** asked on 06 Aug 2021

Is there an equivalent to Telerik.DataSource.DataSourceRequest.ToOdataString() extension for posting to an odata source?

## Answer

**Marin Bratanov** answered on 07 Aug 2021

Hi, This is the extension method we've made for that purpose. The Telerik.Blazor.Extensions namespace exposes that method, you can see it in action here: [https://github.com/telerik/blazor-ui/tree/master/grid/odata](https://github.com/telerik/blazor-ui/tree/master/grid/odata) If this is not what you are looking for, please edit your post to add some more details on the situation. Regards, Marin Bratanov

### Response

**Jstemper** commented on 09 Aug 2021

My question was specifically about posting data changes to an OData source. The examples cites only show getting data from an odata source. Is there any useful extensions for posting data to an odata source?

### Response

**Marin Bratanov** commented on 09 Aug 2021

Thank you for the clarification. We do not and cannot provide API for that as it means serializing the data model, and whether and how that should happen is entirely up to the app. Our components (including the grid) are what we call data-source-agnostic, so they give you events where you get the new data (model) and let the app decide how to handle that (e.g., by sending it to a service which knows how to communicate with the backend).
