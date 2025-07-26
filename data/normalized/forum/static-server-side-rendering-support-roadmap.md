# Static Server-side rendering support roadmap

## Question

**Geo** asked on 04 Mar 2024

Hi Please could you share how you plan to support Blazor SSR mode? Do you intend to make as many components as possible SSR compatible? Do you envisage you will add interactivity to the components in SSR by using JavaScript? Thanks George

## Answer

**Dimo** answered on 07 Mar 2024

Hi George, Can you elaborate which components do you need in static server rendering (SSR) mode and what requires the usage of SSR mode in your case? I must confirm that we don't plan to support SSR at this point. Here are a few more details on the topic: Support for static server rendering practically means to rewrite our components and ignore most of the built-in features of the Blazor framework (component events, repetitive life cycle events, JSInterop). Most of our components are interactive in their essence, so static server rendering doesn't make sense for them. If you need interactive components in SSR mode, then you can use our Kendo UI for jQuery widgets. They will work just fine. You can implement Blazor wrappers for Kendo UI widgets if you prefer (without the JSInterop part). If a lot of customers demand static server rendering support, we can reconsider and make specific tweaks on a case-by-case basis. This brings me back to the question in the begining of my message. Thank you in advance for your insights. Regards, Dimo Progress Telerik

### Response

**George** commented on 15 Mar 2024

Hi Dimo Thanks for your response. I understand it would be a rewrite, or perhaps a separate Telerik Blazor SSR product - which would work somewhat like the ASP.NET Core components, with JS> .NET callbacks. I was just interested in what you were planning in this space. I'd be a bit nervous about using a large JS library such as Kendo UI for jQuery within Blazor without more guidance or ideally it being a supported use case. I'm unsure if enhanced navigation / Streaming Rendering would need disabling for instance. Generally I'd be worried about JS updating the DOM and stepping on Blazor's toes - and vice versa. Any further docs / KB articles you could put together on this would be useful. Thanks George

### Response

**Dimo** commented on 18 Mar 2024

It is true that changing the DOM behind Blazor's back is generally not recommended, because the changes may be lost after the next UI refresh. However, this is a minor concern in SSR mode, because in this case the page behaves pretty much like a "classic" static web page. I am still waiting for information on:>> Can you elaborate which components do you need in static server rendering (SSR) mode and what requires the usage of SSR mode in your case?

### Response

**George** commented on 18 Mar 2024

The priority would be form inputs, I understand the interactivity would need to be handled in JS in this case. A sample creating a Blazor SSR form by wrapping some JQuery components would be helpful. Otherwise for now I think I'd be inclined to stick with MVC/RazorPages over Blazor SSR.

### Response

**Dimo** commented on 18 Mar 2024

>>>> Can you elaborate which components do you need in static server rendering (SSR) mode and what requires the usage of SSR mode in your case?

### Response

**George** commented on 18 Mar 2024

On low interactive sites, the kind one might build with Razor Pages, it's beneficial to avoid WASM start-up time and Server disconnections on poor mobile signal etc.
