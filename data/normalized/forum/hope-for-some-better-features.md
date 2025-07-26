# Hope for some better features

## Question

**wuwu** asked on 19 Feb 2020

The Blarzo UI Is getting better. I just put forward something missing: 1>The Chart UI need: tooltip/datapoint label/Crosshair,Maybe I didn't see an example( except the Pie Chart) 2>The DatePicker/DateTimePicker/NumericTextbox need: Modify data with mouse wheel 3>The DatePicker/DateTimePicker's droplist need: MouseOver effect. 4>In the future,Step by step realized these function Similar to the Aspnet core UI.

## Answer

**Marin Bratanov** answered on 19 Feb 2020

Hello Wu, Here is some information for the things you are looking for: chart: tooltips: You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1412734-tooltips-for-series-data-points](https://feedback.telerik.com/blazor/1412734-tooltips-for-series-data-points) data point label: see how to do it in the documentation: [https://docs.telerik.com/blazor-ui/components/chart/labels-template-and-format](https://docs.telerik.com/blazor-ui/components/chart/labels-template-and-format) crosshair: I made a feature request on your behalf, you can Follow it here: [https://feedback.telerik.com/blazor/1454380-crosshair](https://feedback.telerik.com/blazor/1454380-crosshair) pickers and numeric textbox value changing with the mouse wheel: I would encourage you to post a feature request for such a feature in our Feedback portal through the "Request a Feature" button. Just make sure to select the "make public" checkbox at the final step. This will let you explain your goals, requirements, even perhaps add a sample of what API and functionality you would expect it exposes (for example, how should it be enabled/disabled, what step should it use - especially for the date pickers and time pickers). You can then Vote for it and Follow it to get updates on status changes. If it gets good traction with the community, we will consider its implementation. mouseover for the picker dropdowns: I have logged this for fixing and you can Follow it here (also contains a workaround): [https://feedback.telerik.com/blazor/1454385-calendars-are-missing-mouseover-effect-for-the-dates.](https://feedback.telerik.com/blazor/1454385-calendars-are-missing-mouseover-effect-for-the-dates.) The Time portion of the time pickers has hover effects on my end, though. Could you provide more details on this last question about "step by step like ASP.NET Core UI"? If you are looking for a step-by-step tutorial on using the Telerik Blazor components we have two (for the client and for server flavors). Regards, Marin Bratanov

### Response

**wu** answered on 19 Feb 2020

Oh,Maybe these examples could be done more richly. There are not these controls:Editor/DropDownTree/PivotGrid/Gauges/PDF Viewer, The Chart series is too little,and so on... There are more features when using the UI for AspNet Core. Of course this is a new technology that is still improving. You're one of the few who do this Blazor control library, hoping for a better future.

### Response

**Marin Bratanov** answered on 19 Feb 2020

Hello Wu, If you are looking for a component you don't see, you can go through our Feedback Portal: [https://feedback.telerik.com/blazor.](https://feedback.telerik.com/blazor.) Some are already requested and you can Vote for and Follow them (such as the Html editor and the PDF Viewer ), and you can post new ideas as well, so you can also add your context and needs. By the way, some things can be done already - for example, a textbox, an AnimationContainer and a TreeView can give you a DropDownTree. We will be adding more components, of course, the information from the Feedback portal is used actively in determining which will be the next one we will work on. Blazor has been official for under half a year, and we already have over 30 native components for it. It should be expected that component suites and frameworks that are a decade old should have more components, features and components. Regards, Marin Bratanov

### Response

**wu** answered on 21 Feb 2020

The Blazor Server Demo is too slow because of the network. Recommendations, just suggestions: In future,can you use the WASM framwwork for the Demo,Of cause , It's also slow to load for the first time,Can use on-demand loading technology? This makes less content loaded for the first time.

### Response

**Marin Bratanov** answered on 21 Feb 2020

Hi Wu, This is how the different Blazor flavors are expected to work at this point. Right now, the WASM flavor is not official or supported yet, so we can't use it for our demos. Perhaps we will migrate them to a WASM project when it becomes official, but we can't do it before that. Whether MS will implement some form of load on demand to speed up WASM load times is unkown yet. I have seen an improvement about caching of the resources in their roadmap, so that may help with subsequent loads, but it is unlikely that much can be done for the first load. The first big improvement in this regard would be fixing the linker so we no longer have to disable it when Linq extension methods are present in the code. When that happens, the app size and number of assemblies will drop significantly. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 05 Mar 2020

Hi Wu, There is a feature request for a dropdowntree now, and it contains a sample solution you can use as a starting point. You Vote is already added and you can click the Follow button for status notifications: [https://feedback.telerik.com/blazor/1456580-dropdowntree](https://feedback.telerik.com/blazor/1456580-dropdowntree) Regards, Marin Bratanov
