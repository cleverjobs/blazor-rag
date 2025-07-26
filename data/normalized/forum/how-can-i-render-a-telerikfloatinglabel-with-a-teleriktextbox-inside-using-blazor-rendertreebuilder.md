# How can i render a TelerikFloatingLabel with a TelerikTextBox inside using Blazor RenderTreeBuilder?

## Question

**Phi** asked on 14 Jul 2022

Hey! I searched everywhere but i can't find a solution for my problem. Im using a TelerikTextBox with Telerik Blazor 2.3 but i upgraded to 3.4 and now you have to use a TelerikFloatingLabel as a parent element for the textbox. This is my old code: internal static void CreateLabelTextBox(RenderTreeBuilder builder, int index, string labelContent, string propertyName, object sender, object bindObject, string className, bool isEnabled) { builder.OpenElement(index++, "Div" ); if (! string.IsNullOrEmpty(className)) { builder.AddAttribute(index++, "Class", className); } builder.AddContent(index++, (RenderFragment)((rBuilder)=> { rBuilder.OpenComponent(index++, typeof (TelerikTextBox)); if (! string.IsNullOrEmpty(labelContent)) { rBuilder.AddAttribute(index++, "Label", labelContent); rBuilder.AddAttribute(index++, "Title", labelContent); } rBuilder.AddAttribute(index++, "id", GetNewId()); if (TryGetProperty(propertyName, bindObject, out PropertyInfo property)) { var propertyValue=property.GetValue(bindObject) !=null? property.GetValue(bindObject).ToString() : string.Empty; rBuilder.AddAttribute(index++, "Value", propertyValue); rBuilder.AddAttribute(index++, "ValueChanged", EventCallback.Factory.Create<System.String>(sender, str=> { property.SetValue(bindObject, str); })); } rBuilder.AddAttribute(index++, "Enabled", isEnabled); rBuilder.CloseComponent(); })); builder.CloseElement(); } And now im trying to wrap this inside of a FloatingLabel: internal static void CreateLabelTextBox(RenderTreeBuilder builder, int index, string labelContent, string propertyName, object sender, object bindObject, string className, bool isEnabled) { builder.OpenElement(index++, "Div"); if (!string.IsNullOrEmpty(className)) { builder.AddAttribute(index++, "Class", className); } builder.AddContent(index++, (RenderFragment)((rBuilder)=> { rBuilder.OpenComponent(index++, typeof(TelerikFloatingLabel)); if (!string.IsNullOrEmpty(labelContent)) { rBuilder.AddAttribute(index++, "Text", labelContent); //rBuilder.AddAttribute(index++, "Title", labelContent); } rBuilder.AddContent(index++, (RenderFragment)((xBuilder)=> { xBuilder.OpenComponent(index++, typeof(TelerikTextBox)); //if(TryGetProperty(propertyName, bindObject, out PropertyInfo property)) //{ // var propertyValue=property.GetValue(bindObject) !=null ? property.GetValue(bindObject).ToString() : string.Empty; // xBuilder.AddAttribute(index++, "bind-Value", propertyValue); //} xBuilder.CloseComponent(); })); rBuilder.CloseComponent(); })); builder.CloseElement(); } Any suggestions how this might work?

### Response

**Marin Bratanov** commented on 16 Jul 2022

I would personally not do that - it is very error prone and difficult to maintain. If you want something reusable that cannot be a component, you can use a C# method with the HTML in it like this Grid dynamic column template example.

### Response

**Philipp** commented on 17 Jul 2022

Thank you very much.
