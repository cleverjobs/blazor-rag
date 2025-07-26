# Telerik Plans for integrating AI into Blazor Components

## Question

**TomTom** asked on 04 Oct 2024

I`m looking to improve the UX around the Editor Component and to incorporate grammar/rewrite capabilities. It seems Telerik Components are bit light when it comes to AI integration and don`t see anything on the roadmap either. For comparison Syncfusion have a whole set of integrations ( Introducing the AI-Powered Smart Blazor Components and Features (syncfusion.com) ) and specifically one for their Editor which gives it grammar/rewrite/summarisation capabilities. All I`ve found from Telerik is the AI Prompt which is only useful if you`re looking for a chatbot experience.

## Answer

**Dimo** answered on 04 Oct 2024

Hi Tom, Please check the Blazor Lab section on our demo site for AI examples. It is important to note that all AI functionality that we show is completely detached from the Telerik UI for Blazor product. The existing online examples aim to showcase sample integration, create hype, and gather customer feedback. We have no plans to integrate AI as a built-in feature into our components, because this may pose privacy or security concerns for our customers and is outside the scope of our product. Of course, our UI components can be used in application scenarios that involve the use of AI. In this specific case, you can implement a custom Editor tool that shows a popup. There the user can perform AI-related actions which then change the Editor Value programmatically. Regards, Dimo Progress Telerik
