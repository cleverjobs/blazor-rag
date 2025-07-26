# TelerikRootComponent in MVC

## Question

**Bil** asked on 06 Jan 2025

We have a legacy ASP.NET Core MVC app and are migrating it to Blazor Interactive Server one view/page at a time. We have Blazor Interactive Razor Components in a MVC Razor View working. What is the guidance on the TelerikRootComponent in this scenario? There is no Blazor interactive layout file to place it in w/ this use case. <div class="alert alert-dark" role="alert"> This is an ASP.NET Core MVC Razor View/Page. </div> <div class="card"> <div class="card-header"> Blazor Interactive Server Component </div> <div class="card-body"> <component type="typeof(MyWeb.Components.Tests.Test)" render-mode="ServerPrerendered" /> </div> </div>

## Answer

**Hristian Stefanov** answered on 09 Jan 2025

Hi Bill, In your scenario of integrating Blazor components into an existing ASP.NET Core MVC application, the TelerikRootComponent plays a crucial role in ensuring that Telerik UI components are initialized and function correctly. Here's how to approach this: Placement of TelerikRootComponent: Since your application doesn't have a Blazor interactive layout file, you should place the TelerikRootComponent within the MVC Razor View that contains the Blazor components. This component acts as a root for all Telerik UI components and ensures their proper initialization. Including TelerikRootComponent: You can add the TelerikRootComponent directly in your Razor View by wrapping it around the Blazor components you are rendering. Here's an example of how to structure it: <div class="alert alert-dark" role="alert"> This is an ASP.NET Core MVC Razor View/Page. </div> <div class="card"> <div class="card-header"> Blazor Interactive Server Component </div> <div class="card-body"> <TelerikRootComponent> <component type="typeof(MyWeb.Components.Tests.Test)" render-mode="ServerPrerendered" /> </TelerikRootComponent> </div> </div> Script References: Ensure that all necessary Telerik scripts are included in your layout or view. This is crucial for the proper functioning of the Telerik components. Check that these scripts are loaded correctly in your application. Regards, Hristian Stefanov Progress Telerik

### Response

**Bill** commented on 09 Jan 2025

Wrapping the Blazor component with aTelerikRootComponent tag in an MVC view does not work. You get exceptions that the TelerikRootComponent is required when attempting to use Telerik components within the MyWeb.Components.Tests.Test component. However, wrapping the TelerikRootComponent around all inside the MyWeb.Components.Tests.Test component works, but I've experienced issues in the past where popups/etc positioning will not work like this (wrapping 1 component at a time) unless you place the TelerikRootComponent at the root of the DOM (wrap everything (all body content) inside of it - typically in a Layout file). When upgrading a legacy MVC application, we need to upgrade/create 1 component per page/view at a time. The shell/layout is MVC, so we can't adhere to documented TelerikRootComponent guidance and I fear our use of Telerik will not work properly. It only works in a native Blazor app, not 1 component at a time within an MVC app.

### Response

**Bill** commented on 09 Jan 2025

And just as I feared, wrapping the TelerikRootComponent within MyWeb.Components.Tests.Test around all else results in popups being misaligned. Check this screenshot of the Telerik Grid. I clicked the Filter column menu button and the popup menu displays off the page (far right). Is this a deal breaker where we cannot use Telerik for upgrading MVC apps in a "mixed mode"?

### Response

**Hristian Stefanov** commented on 10 Jan 2025

Hi Bill, Incorrect popup positioning is expected when the TelerikRootComponent does not wrap all the elements. I apologize for not providing sufficient detail in my initial suggestion. We have a dedicated section in our documentation that explains this behavior in detail: Wrong Popup Position. In summary, the issue arises because the TelerikRootComponent does not wrap all elements and is not the topmost element. To resolve this, try placing everything currently outside the component (as highlighted below) within the Blazor component, ensuring that the TelerikRootComponent serves as the outer wrapper for all the visible content on the page. <div class="alert alert-dark" role="alert"> This is an ASP.NET Core MVC Razor View/Page. </div> <div class="card"> <div class="card-header"> Blazor Interactive Server Component </div> <div class="card-body"> <component type="typeof(MyWeb.Components.Tests.Test)" render-mode="ServerPrerendered" /> </div> </div> Kind Regards, Hristian

### Response

**Bill** commented on 10 Jan 2025

Because the app is an MVC app, we can't wrap the TelerikRootComponent around all that you highlighted. We can only wrap the contents of what's inside the MyWeb.Components.Tests.Test Blazor component. That's the premise of this thread post. Is there a workaround when we cannot place the TelerikRootComponent with the <body> or root/entire viewport? We are converting one MVC razor view at a time to Blazor. The "shell"/layout of the app is still MVC, not Blazor.

### Response

**Hristian Stefanov** commented on 14 Jan 2025

Hi Bill, The TelerikRootComponent wrapping everything is essential for proper popup placement. I confirm that this is a requirement, and there isn’t a workaround for it. Kind Regards, Hristian
