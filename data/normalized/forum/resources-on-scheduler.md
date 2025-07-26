# Resources on scheduler

## Question

**JKa** asked on 20 Jan 2020

Today i use the WPF scheduler for my planning application and i would like to experminent with the Blazor scheduler. My current scheduler uses a multiday view with horizontal the days with the hours, vertical i use the equipments as resource to view the appointments for the equipments. I wonder if this can be achieved with the current component

## Answer

**Marin Bratanov** answered on 20 Jan 2020

Hi, The current resource implementation in the Blazor scheduler colors the appointments according to the resource color: [https://docs.telerik.com/blazor-ui/components/scheduler/resources.](https://docs.telerik.com/blazor-ui/components/scheduler/resources.) Would the grouping feature you seek look something like this: [https://demos.telerik.com/aspnet-core/scheduler/resources-grouping-vertical?](https://demos.telerik.com/aspnet-core/scheduler/resources-grouping-vertical?) I am asking so I can make sure I understand what you need and create an appropriate feature request for you (of course, you could do that yourself - click the "Request a Feature" button at the top right here, and make sure to select the "make public" checkbox at the final step - this will let you add the context, any relevent links/screenshots and how you would expect this to be exposed for configuration). In the

### Response

**JKattestaart** answered on 21 Jan 2020

Yes, a timeline view is actually what i want. I see it's already on the feature requests thnx

### Response

**Marin Bratanov** answered on 21 Jan 2020

Hello, If you are referring to a timeline like this one: [https://demos.telerik.com/aspnet-core/scheduler/timeline](https://demos.telerik.com/aspnet-core/scheduler/timeline) I must note that this particular example also uses grouping for the resources. A plain timeline view would not list the resources on the left like that, the grouping is a separate feature. Here's how a timeline would look like without grouping: [https://dojo.telerik.com/@bratanov/UJIciheZ.](https://dojo.telerik.com/@bratanov/UJIciheZ.) If this isn't what you are after, maybe we should create a separate feature request for grouping, as it is not likely to get implemented together with a new view. For anyone else, here is the feature request for a timeline view in the Blazor scheduler: [https://feedback.telerik.com/blazor/1446466-timeline-view](https://feedback.telerik.com/blazor/1446466-timeline-view) Regards, Marin Bratanov
