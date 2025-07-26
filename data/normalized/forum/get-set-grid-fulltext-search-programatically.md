# Get / Set grid fulltext search programatically

## Question

**Lie** asked on 23 Feb 2021

Is there a way to access the fulltext search value programatically? I have three scenarios in my mind: 1. My customer requested a button to clear all filters, resp. reset the grid to it's initial state 2. I would like to use external textbox for the fulltext filtering. Sometimes it just doesn't fit into the grid toolbar and I need it to be outside the grid. 3. I would like to use querystring for setting innitial value of the fulltext filter.

## Answer

**Marin Bratanov** answered on 23 Feb 2021

Hello Liero, For ability to get and set the built-in searchbox value, Follow this: [https://feedback.telerik.com/blazor/1494717-ability-to-clear-the-searchbox-on-escape-key-with-an-x-in-the-input-and-programmatically.](https://feedback.telerik.com/blazor/1494717-ability-to-clear-the-searchbox-on-escape-key-with-an-x-in-the-input-and-programmatically.) It will probably expose two-way binding for the value so you can get or set it in your view-model as needed (you could clear it, or you could set it from the querystring). I've added your Vote to it on your behalf to raise its priority, and you can also click the Follow button to get email notifications for status changes. As for an external searchbox, you'd have to do the work we do behind the scenes - you need to add custom filter descriptors to your grid for all fields you want to filter. You can find examples in the State article (see also the second set of snippets about setting filters): [https://docs.telerik.com/blazor-ui/components/grid/state#set-grid-options-through-state](https://docs.telerik.com/blazor-ui/components/grid/state#set-grid-options-through-state) Regards, Marin Bratanov

### Response

**Liero** answered on 23 Feb 2021

If there was a two way binding, it would work with the external searchbox wouldn't it? I mean there is no need to require the actual GridSearchBox component within the toolbar once there is a parameter property, right?

### Response

**Marin Bratanov** answered on 23 Feb 2021

Hi Liero, The Value of the search box would be exposed on the built-in searchbox component, not on the grid. So, to use it you would still need the built-in searchbox. Regards, Marin Bratanov

### Response

**Liero** answered on 03 Mar 2021

Doesn't it make more sense, to have the FulltextSearch property on the Grid and just bind the SearchBox to the property? It would be quite helpful in my scenario. BTW, that's how ag-grid and syncfusion does it. Just teasing :)

### Response

**Marin Bratanov** answered on 03 Mar 2021

Hello, At this point I think that using two-way binding for the GridSearchBox component is the cleanest way to do this because the whole searchbox functionality is kind of separate from the grid filters and having it encapsulated in its own component does have benefits (like keeping all the features related to it in one place, instead of scattered across several tags). Moreover, it would open the door for other functionality like clearing those filters programmatically, and keyboard support for that field. In other words, that input would act like a real blazor input, not an input without two-way binding. If you really want your users to not have the searchbox in the UI, you can either build a list of filter descriptors on your own without the grid feature, or you could hide the searchbox with CSS from the grid toolbar. Regards, Marin Bratanov
