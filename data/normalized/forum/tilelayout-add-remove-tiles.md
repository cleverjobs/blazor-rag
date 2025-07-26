# Tilelayout Add-remove tiles

## Question

**Pau** asked on 20 May 2022

Hi I saw this demo: [https://github.com/telerik/blazor-ui/tree/master/tilelayout/add-remove-tiles](https://github.com/telerik/blazor-ui/tree/master/tilelayout/add-remove-tiles) It looks great but its added code. So it would be nice to have this behavior build into the component: 1. Have a property with a list of available components 2. have the component let the user pick from a list (The list could be a dropdown value list) 3. With saving state also save the connected component 4. have an event on which we instantiate the component when the layout is shown Eric

## Answer

**Svetoslav Dimitrov** answered on 25 May 2022

Hello Eric, The TileLayout is a completely templated component. In the <Content> you can place any arbitrary HTML - from something as simple as ul with li items to a complex component like the Grid. At runtime, the framework does not provide us with a way to get the content of a RenderFragment (the <Content> is a RenderFragment). For us to provide this as a built-in behavior we must have the content of the tilelayout tiles first, which is something that is not possible at the moment. This is why you would need to add some custom logic that is aware of the aware of what is content of the tiles, thus we created this sample demo to showcase that concept. Regards, Svetoslav Dimitrov

### Response

**Paul** commented on 25 May 2022

Hi As you can see in the demo, blazor components are loaded, not arbitray HTML. Have you seen the demo? Eric

### Response

**Svetoslav Dimitrov** commented on 27 May 2022

Hello Eric, The Telerik UI for Blazor components are rendered as plain HTML in the DOM tree. On runtime we, as a vendor, cannot obtain the information on which components are rendered, only the application has that knowledge. For example, the Grid is rendered as a complex <table> HTML element. I am aware of the implementation of the demo sample from the blazor-ui public GitHub repository and until (if) the Blazor framework provides us with a built-in way to obtain the content of the RenderFragment on runtime, this demo is the best possible way to move forward.
