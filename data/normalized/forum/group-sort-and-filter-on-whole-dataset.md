# Group, sort and filter on whole dataset

## Question

**EdEd** asked on 12 Apr 2020

Hi, It seems as though these things only work on the current page. Is there a way to do these things at teh dataset level? Any guidance would be great! Thanks .... Ed

## Answer

Hello Ed, Where the data comes from depends entirely on the app. While our documentation usually uses some data generated in the view-model for brevity, you have full flexibility over the data source. For example: You can optimize data binding in two common ways: With server-side Blazor, you can directly use an IQueriable collection tied to your backend/service You can implement your own data source operations through the OnRead event and call a WebAPI or OData endpoint, or any other service of yours (by the way, our next 2.11.0 will allow you to serialize the DataSourceRequest object). You can read more about this in the grid data binding documentation: [https://docs.telerik.com/blazor-ui/components/grid/columns/bound#notes](https://docs.telerik.com/blazor-ui/components/grid/columns/bound#notes) You can verify that using a database works seamlessly (of course, through a service) from our live demos: (For instance, try to search for Product 45): [https://demos.telerik.com/blazor-ui/grid/filter-row](https://demos.telerik.com/blazor-ui/grid/filter-row) Regards, Eyup
