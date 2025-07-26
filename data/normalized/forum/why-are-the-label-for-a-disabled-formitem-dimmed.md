# Why are the Label for a disabled FormItem dimmed?

## Question

**Mar** asked on 20 Jan 2023

I want some properties to be read-only. I am okay with the disable style on the textbox, that's standard. But why dimme the label? Whats the best way to make the label normal again?

## Answer

**Nadezhda Tacheva** answered on 25 Jan 2023

Hi Martin, The built-in label is a part of the form field. If you inspect the rendering, you may notice that both the label and the input are nested in a <div class="k-form-field">. By design, when the form field is disabled, "k-disabled" class is added to that div. In this case, its children - the label and the input - both have certain styling that indicates to the user this field is not editable. You have two options to customize this behavior: If you use the Enabled="false" property of the form field, the label will be disabled by default and you may apply some CSS to the label to style it as needed. If you use a FormItem Template you may override the default rendering. In this case, you may not disable the whole field but just the custom input inside it. For example: [https://blazorrepl.telerik.com/mdubcpEV50medcHl00.](https://blazorrepl.telerik.com/mdubcpEV50medcHl00.) I hope you will find this information useful to move forward with your application. Please let me know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Martin Herløv** commented on 25 Jan 2023

I have tried to style the label but with no luck. I can't remove the grayfilter. Could you provide some css for me?

### Response

**Nadezhda Tacheva** commented on 27 Jan 2023

Hi Martin, The styles for the disabled state propagate to the label from its parent <div class="k-form-field k-disabled">. The "k-disabled" class reduces the opacity of the whole field and it is not possible to override that by targeting just the label. So, I will list another approach based on CSS. Do not use the Enabled parameter of the FormItem to mark the whole field as disabled. Instead, add your custom class to it and add styles to disable just the input and not the label. Here is an example: [https://blazorrepl.telerik.com/GnkFQhFq48jV2UZs08.](https://blazorrepl.telerik.com/GnkFQhFq48jV2UZs08.) I hope this helps.

### Response

**Martin Herløv** commented on 27 Jan 2023

Thank's, just what I wanted

### Response

**Nadezhda Tacheva** commented on 01 Feb 2023

Hi Martin, I am glad to find out my suggestion helped you to achieve your desired result. Please let us know if you are experiencing any other difficulties.
