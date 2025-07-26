# Creating custom bundle for controls

## Question

**Aar** asked on 25 Nov 2020

I am using Telerik UI for Blazor. I am planning to reduce the size of JavaScript bundle used for Telerik UI blazor components. So how to create the custom bundle for particular components. so that I can reduce the page load time. Can anyone help me on this!!

## Answer

**Marin Bratanov** answered on 25 Nov 2020

Hello Aartheeswaran, When the source code becomes available, you could try tweaking such things. You can Follow when that happens here. I must note that our JS file is rather small, especially compared to other suites of web components. We use JS only when absolutely necessary as our components are completely native. Thus, such a reduction would be rather difficult and would not bring much benefit. Regards, Marin Bratanov

### Response

**Aartheeswaran** answered on 25 Nov 2020

Hi Marin, Thank you for your quick response. For your information we already have license of Telerik UI for Blazor components. we have found Kendo UI have custom downloads like this ([https://www.telerik.com/download/custom-download).](https://www.telerik.com/download/custom-download).) we are searching custom download for Telerik UI for blazor components. Please guide me to the right path if I am wrong.

### Response

**Marin Bratanov** answered on 25 Nov 2020

Hello Aartheeswaran, The Kendo widgets are jQuery plugins and it makes sense to be able to split them up. Moreover, their JS file is rathre on the large side. The Blazor components, however, are NOT jQuery plugins, but native components and such splitting of resources will make them very hard to use. So, there are no plans to make them "splittable". Optimization techniques you can look into are: using the defer attribute on our js file, like we show in our demos - it lets the browser parse it a little later. This is especially helpful if your landing page does not use telerik components adding the telerik theme stylesheet later (e.g., with JS Interop when a page that uses the telerik components is requested) if you create a custom theme you could only add some components to it to reduce its size. lazy-loading the telerik assemblies if you are using a web assembly project (see here for a sample project) any general performance optimizations as described in this article. Regards, Marin Bratanov

### Response

**Aartheeswaran** answered on 25 Nov 2020

Hi Marin, Thank you for your detailed explanation
