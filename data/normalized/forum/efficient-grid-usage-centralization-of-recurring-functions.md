# Efficient Grid Usage: Centralization of Recurring Functions

## Question

**Hen** asked on 20 Mar 2025

I use the grid in many places, and I would like not to have to reimplement recurring tasks, such as state management or Excel export, every time. I have thought about using a custom wrapper, but that is very laborious and complicated. Is there an elegant way to centralize some functions?

## Answer

**Anislav** answered on 20 Mar 2025

Hi Hendrik, You can reuse code by either inheriting from or wrapping Telerik components. There is a basic article that provides some information on this topic: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/common-extend-inherit-wrap-reuse-telerik-blazor-components.](https://www.telerik.com/blazor-ui/documentation/knowledge-base/common-extend-inherit-wrap-reuse-telerik-blazor-components.) I believe that wrapping the components is a better approach. Blazor provides several features that can help with this, including: Attribute splatting and arbitrary parameters: [https://learn.microsoft.com/en-us/aspnet/core/blazor/components/splat-attributes-and-arbitrary-parameters](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/splat-attributes-and-arbitrary-parameters) Dynamically-rendered components: [https://learn.microsoft.com/en-us/aspnet/core/blazor/components/dynamiccomponent](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/dynamiccomponent) Templated components: [https://learn.microsoft.com/en-us/aspnet/core/blazor/components/templated-components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/templated-components) Regards, Anislav Atanasov

### Response

**Hendrik** commented on 21 Mar 2025

Thank you very much for your support. I discovered a way to integrate the grid into a wrapper while retaining all its features—such as aggregates, details, and so on—without duplicating any functionality within the wrapper.

### Response

**Anislav** commented on 21 Mar 2025

If you're open to it, feel free to share some of the code. I'd be happy to review it and provide feedback—it could also help others looking for a similar approach! Regards, Anislav Atanasov

### Response

**Hendrik** commented on 21 Mar 2025

Yes, I am open to it but I have to build an extra sample. Can not use my actual code. But my solution should be helpful to other users. I am always thinking of a kind of "Community Toolkit" where to find samples and best-practices. The samples from Telerik are often outdated and hard to get running... Why is nobody updating those samples !?

### Response

**Dimo** commented on 25 Mar 2025

@Hendrik - Can you please specify which outdated samples are you referring to? If you are talking about the ones in the blazor-ui repo, indeed, some of them are quite old. We have an ongoing effort to: Remove the ones that can be replaced with KB articles in the documentation. For example: Responsive Form Single Notification instance Responsive Grid behaviors Update the ones that should remain there. For example: Localization sample apps Let me know if you have stumbled upon anything specific that you feel should be updated. All examples in the documentation should be up-to-date, unless they target an old product version by design.

### Response

**Hendrik** commented on 25 Mar 2025

Yes, I mean the samples in the repo. The samples in the online documentation and samples are good, but some tricks are only covered in the repo. Btw: I am always stumbeling over TelerikMessages.resx that supposed to take from the repo. But it is also outdated and I get errors when newer components have new descriptions...

### Response

**Dimo** commented on 25 Mar 2025

The location of up-to-date localization .resx files is documented at Localization - Add Resource Files

### Response

**Hendrik** commented on 25 Mar 2025

Thank you for that hint. I took it always from the demo-repo. Maybe I misunderstood something...
