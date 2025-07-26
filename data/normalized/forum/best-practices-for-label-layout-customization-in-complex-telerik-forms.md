# Best Practices for Label Layout Customization in Complex Telerik Forms

## Question

**Boh** asked on 03 Jun 2025

Hello Telerik Team, I'm building advanced forms using <TelerikForm> and <FormItem> components. My use case includes complex grid layouts (4+ columns), dynamic label/input structures, and the ability to switch orientations (horizontal ↔ vertical) depending on the layout. The problem I face is related to label positioning and flexibility. Since labels are tightly bound to inputs inside <FormItem>, it's hard to restructure the layout dynamically or follow modern design principles where labels float, stack, or separate cleanly from inputs. Additionally, because <FormItem> doesn’t offer properties like LabelCssClass or FieldCssClass, I’m forced to use <Template> for nearly every form element. And in large forms (50+ fields), that creates a huge boilerplate mess. Here's a code example of how I currently break label/input pairing just to achieve layout control: <FormItem Field="Number1" ColSpan="2"> <Template> <label for="Number" class="k-label k-form-label"> @Localizer["Form_JednAdminView_Number"]: </label> </Template> </FormItem> <FormItem Field="Number1" ColSpan="1"> <Template> <TelerikNumericTextBox Id="Number1" Value="@DataContext.FormData.Number1" ValueExpression="@(()=> DataContext.FormData.Number1)" ReadOnly="true" /> <TelerikValidationTooltip For="@(()=> DataContext.FormData.Number1)" TargetSelector="#Number1" /> </Template> </FormItem> <FormItem Field="Number2" ColSpan="1"> <Template> <TelerikTextBox Id="Number2" Value="@DataContext.FormData.Number2" ValueExpression="@(()=> DataContext.FormData.Number2)" ReadOnly="true" /> <TelerikValidationTooltip For="@(()=> DataContext.FormData.Number2)" TargetSelector="#Number2" /> </Template> </FormItem> @GetEmptyFormItem(4) Some notes about the limitations: -I cannot use RenderFragment loops with a shared template to render controls dynamically — because I lose the ability to manage each control’s UI and behavior precisely. -Using @refs to manage these dynamic elements becomes a nightmare — they don't give me flexible access to the rendered markup/UI, and the logic becomes very hard to maintain. -So to preserve clean control over layout and per-control behavior, I'm forced to manually write each <FormItem> and control in a verbose way — which feels like overkill. In aim to have les s boilerplate UI and code, but still have an ability to change layout structure in real time - my questions are: -Can we request a feature to separate labels from inputs, but still associate them logically (e.g., via an Id, or LabelFor property)? -Is there any plan or recommendation to make <TelerikForm> more flexible — for instance, to allow label placement (above/beside) or wrapping via a simple layout option? -Are there any workarounds/best practices for advanced layouts with full control over label/input rendering, while preserving strong typing and validation? But the main aim is to have an opportunity to have Labels aligned by left and have "space between" input and label, Maybe there is some easy approach with overriding some of your classes like k-input or k-label or k-form-label etc...? I’d really appreciate your insights. Thanks for your time and help! Best regards, Bohdan (Blazor Developer)

### Response

**Bohdan** commented on 03 Jun 2025

If there are any questions about it - feel free to ask=)

## Answer

**Dimo** answered on 03 Jun 2025

Hi Bohdan, The requested enhancements are already possible with a FormItem <Template> and <FormItemsTemplate>. You can also apply custom styles to Form labels, input containers and inputs through the Class parameter of FormItem: <TelerikForm> <FormItems> <FormItem Class="blue-label red-textbox"> </FormItem> </FormItems> </TelerikForm> <style>.blue-label.k-label { color: blue; background: yellow;
}.red-textbox.k-form-field-wrap.k-input { border-color: red;
} </style> Built-in support for separate label tags with arbitrary position sounds like an enhancement that won't justify the development effort and customer demand, but I will discuss this with the team. If you are concerned about too much boilerplate, you can implement custom reusable Razor components. On a side note, we have a feature request about a Form layout enhancement that may be relevant to your needs. Regards, Dimo Progress Telerik

### Response

**Bohdan** commented on 03 Jun 2025

Thanks for your response. I see your point about overriding classes, and while it helps with label styling, the problem is deeper: Once I start customizing label layout via CSS inside a <Template>, I lose all grid-like behavior and column alignment provided by the FormItem’s layout engine. That means I have to manually manage spacing, alignment, and responsiveness — which defeats the purpose of using Telerik’s built-in form layout system. That’s why I was wondering if there’s a more official or recommended way (or future plan) to support separate label/input structures — but still let them participate in column spans, alignment, and layout consistency. Otherwise, every small layout change turns into boilerplate CSS and Template juggling, and for large forms this becomes very hard to maintain. Thank you so much for answer!

### Response

**Dimo** commented on 03 Jun 2025

Our documentation shows how to use labels inside a template, so that all the original styling is preserved.
