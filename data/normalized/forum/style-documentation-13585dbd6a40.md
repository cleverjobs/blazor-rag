# Style documentation

## Question

**Den** asked on 07 May 2020

Hi, I was looking for a badge and I couldn't find any description like bootstrap has on its components ([https://getbootstrap.com/docs/4.0/components/badge/).](https://getbootstrap.com/docs/4.0/components/badge/).) Where can I find something similar to this for Blazor UI? Thanks in advance

## Answer

**Marin Bratanov** answered on 07 May 2020

Hello Dennis, The Bootstrap badge features are something you can use as-is in a Blazor app - it's just a collection of HTML and some CSS classes. You can even wrap it in a component of yours to reuse more easily. That's one of the reasons why we don't have an explicit badge component - there are many ways to do one, and the layout frameworks (such as bootstrap) that people already use tend to have such functionality, so it does not make much sense for us to create a clone or wrapper for them. That said, am I missing something? Would you be expecting us to document Bootstrap features or to create wrappers for them? Regards, Marin Bratanov

### Response

**Dennis** answered on 07 May 2020

Thanks for the quick reply. I'm new to your product and I didn't know that it's alike the Bootstrap components. So I can just use the Bootstrap equivalent classes and just add a 'k-' before it to get the Telerik themed style?

### Response

**Marin Bratanov** answered on 07 May 2020

Hello Dennis, We do not implement Bootstrap capabilities at all, we let Bootstrap do that, our components can simply plug into those layouts. You can read more about this in the Bootstrap notes section of our docs: [https://docs.telerik.com/blazor-ui/themes/overview#bootstrap-notes](https://docs.telerik.com/blazor-ui/themes/overview#bootstrap-notes) In other words, you cannot and should not prefix the bootstrap classes with "k-". Regards, Marin Bratanov

### Response

**Dennis** answered on 07 May 2020

Maybe I formulated my question wrong. I created a custom theme based on the default theme using the Sass Themebuilder ([https://themebuilder.telerik.com/blazor-ui?_ga=2.179269156.1686381975.1588852406-83752003.1573200327)](https://themebuilder.telerik.com/blazor-ui?_ga=2.179269156.1686381975.1588852406-83752003.1573200327)) and added it to my project. I wanted a badge, so I looked at the generated css file and in [https://docs.telerik.com/blazor-ui/themes/form-elements](https://docs.telerik.com/blazor-ui/themes/form-elements) and saw the 'k-' prefix. That's why I asked. I don't want the use Bootstrap, but the default Telerik theme. What is the correct way to get a badge with the custom theme?

### Response

**Marin Bratanov** answered on 07 May 2020

Hi Dennis, You can see what the colors are in the variables.scss file so you can use them in your site specific stylesheets to style custom badges or to override the Bootstrap one. If you are OK with the bootstrap styles, use bootstrap. At the moment, there are no Telerik Badge component or classes you can use readily. I also made the following feature request page on our portal so you can Follow the implementation of a Telerik Badge component: [https://feedback.telerik.com/blazor/1465161-badge-component.](https://feedback.telerik.com/blazor/1465161-badge-component.) If it gains enough traction with the community, we will consider its implementation. Regards, Marin Bratanov

### Response

**Dennis** answered on 08 May 2020

Many thanks for the feature request. I was wondering if the generated css from the Sass Themebuilder remains (almost) the same. The generated css file already contains the classes for the component(s). So if you stick with these, you only have to write some documentation for it. Best regards, Dennis PS: css class of badge found in the generated css file: .k-badge-primary { border-color: #9e2d94; color: #fff; background-color: #9e2d94; } .k-badge- circle { padding: 0!important; width: calc( 1em + 10px ); height: calc( 1em + 10px ); border-radius: 100%; } .k-badge { margin: 0 0 0. 5em; padding: 4px 4px; border-width: 1px; border-style: solid; border-color: transparent; box-sizing: border-box; color: inherit; background-color: transparent; font-size: 10px; line-height: 1; text-align: center; white-space: nowrap; display: -ms-inline-flexbox; display: inline-flex; -ms-flex-align: center; align-items: center; -ms-flex-pack: center; justify- content: center; vertical-align: middle; overflow: hidden; text- overflow: ellipsis; }

### Response

**Marin Bratanov** answered on 08 May 2020

Hi Dennis, These classes and their content may change if the components and themes need to evolve. They are not something we will document per-se, because those classes are meant for our internal use - they rely on combinations between them, on certain HTML structure and may have other requirements (such as adding/removing some of them dynamically to achieve certain results). This is not something that is document-able. If you want to try to emulate badges, you can consider inspecting what the Kendo UI for jQuery badge renders after initialization and try to mimic its HTML structure. Regards, Marin Bratanov
