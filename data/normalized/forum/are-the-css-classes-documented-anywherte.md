# Are the css classes documented anywherte?

## Question

**Joh** asked on 27 Jun 2021

I've noticed I cannot just use straight bootstrap with telerik components and I have noticed that the majority of demos/samples use styling/placement such as k-textbox, k-col-start-6 and much more. I have no idea what these are doing or how they are used. I've used bootstrap because there is excellent support for flex and the concepts are not overly difficult. Is there any similar documentation for all the k- classes? Trying to do a simple two-column layout. each column has multiple field groups on a single row. Pseudo-code form-row col-md-6
form-group col-md-6
Label
TelerikTextBox
form-group col-md-2
Label
TelerikTextBox
form-group col-md3
Label
TelerikTextBox
col-md-6
form-group col-md-6
Label
TelerikTextBox
form-group col-md-2
Label
TelerikTextBox
form-group col-md3
Label
TelerikTextBox Ok, I got one step closer. Use fieldset instead of trying to use grid system solely: <div class="form-row"> <div class="col-md-6"> <fieldset id="LeftColumn" name="LeftColumn"> <legend> </legend> <div class="form-group"> <label> </label> <input /> </div> <div class="form-row"> <div class="col-md-8"> <label </label> <input /> </div> <div class="col-md-2"> <label> </label> <input /> </div> <div class="col-md-2"> <label> </label> <input /> </div> </div> </fieldset> <fieldset id="RightColumn" name="RightColumn"> <legend> </legend> <div class="form-group"> <label> </label> <input /> </div> <div class="form-row"> <div class="col-md-8"> <label </label> <input /> </div> <div class="col-md-2"> <label> </label> <input /> </div> <div class="col-md-2"> <label> </label> <input /> </div> </div> </fieldset> </div> </div> However, fieldset does NOT have the customary border around it. So, we're back to trying to figuring out your CSS classes again. because there is no documentation.

### Response

**Daniel** commented on 28 Jun 2021

+1 It's really annoying that you use classes in the examples and even in the documentation. But no documentation about the classes. So we have to guess.

### Response

**John** commented on 28 Jun 2021

The components seem decent enough but I'd recommend against their use if the documentation sucks. And right now, I consider it minimalistic. Not ready for me to recommend to my user group nor to my employer (20k+ developers). I mean, seriously... pay $899 plus $450 a year just for the name? There's lots of smaller component libraries being created by smart guys with just as much documentation as this.

### Response

**Blazorist** commented on 28 Jun 2021

I've face the same problem a couple months ago. No documentation is provided and as Daniel said, is really annoying and a constant waste of time. I speed up installing a VS extension that show a preview of the styles while you type.

## Answer

**Dimo** answered on 28 Jun 2021

Hello John, Daniel, Your posts touch several different topics, so let me try address all of them: Bootstrap compatibility Our components ship with a "Bootstrap" theme, which makes them look consistent with the Bootstrap library interface. However, our products do not use the Bootstrap CSS classes. The reason is that we cannot depend on a third-party library for our styling. On the other hand, there is no problem to create a Bootstrap column layout and place our textbox components in it. In case you wish our textboxes (or ComboBoxes, DatePickers, etc.) to adjust their width, according to the Bootstrap column widths, please set Width="100%" as a component attribute. k-classes breaking generic HTML elements' appearance John's edit suggests that this is a specific perceived issue: "fieldset does NOT have the customary border around it. So, we're back to trying to figuring out your CSS classes again." The fieldset border is removed by the Bootstrap library stylesheet, not by us. We do not reset the appearance of HTML elements that are unrelated to our product. Classes used in our demos or documentation The CSS styles that we use in our online resources are not required by the built-in functionality of our products. We may add some custom styles to the demos just to improve the UI. Surely, if you point to a page where there is a need to know more about a specific CSS class usage, do let us know and we will add more information. Documenting the k-classes Indeed, currently we have no documentation about the k-classes, because such is rarely needed. Normally, a developer will create a custom theme with our Blazor ThemeBuilder to use a different color scheme. This process does not require knowledge about the k-classes. Advanced customization may involve changing the components' sizing, but the k-classes don't participate in this process either. Which leaves just one case when these classes are needed - when you need to tweak a specific element in a specific way. The easier way to do this is to open the browser's web inspector, see what is the CSS class and current styles, and create a custom CSS rule to apply different styles. The number of possible scenarios here is unlimited, so I can't imagine documentation that can be specific and useful enough. Nevertheless, if you share what type of documentation you expect and how you intend to use it, we will consider adding it. Regards, Dimo Progress Telerik

### Response

**John** commented on 28 Jun 2021

Ok Dimo. I'll take you up on that last point. Telerik publishes demos and samples with specific k-classes all over the place. If you use it, document it. Solved it. I am trying out the components for their functionality -and- the UI/UX. You've documented the one side but not the other. Its like "see this pretty little box we're showing you? tough luck jack, it doesn't look like that when YOU do it." That grates. For example, in the Windows Demo, the following classes are used: k-form, k-form-fieldset, k-form-legend, k-form-field, k-textbox. And that is not including anything tag-specific in the demo. I copy that code *exactly* minus the classes and it sure doesn't look like THAT (the demo). So, to replicate what Telerik has done requires me to do an in-depth analysis of your css just to get something looking similar to the demo. I assume you can see the reason for the frustration. I *know* there is some kind of css override for the legend tag since *I* don't get a nice underline on my legends. And there is no css class used for legend. If you publish it, document it. We may not WANT to use the same things as you pointed out. And it may not be your fault that something isn't HTML standard (the bootstrap fieldset example). But please document what you DO publish. If could be as simple as including the specific styles used in the example so that they are visible, i.e. <style></style>

### Response

**Dimo** commented on 30 Jun 2021

Thanks for sharing your experience in detail. I am sorry that our examples made you feel that way. I get the impression that the main goal here is to use k-classes to style generic HTML elements. This approach is reasonable only for a small subset of the k-classes. Some of them are already documented. We will add a few more, but only those that can be reused universally and safely. Otherwise we will put ourselves in a situation to document, support and encourage using something that is similar to a private API. If you wish to implement a good looking form with our own officially supported and documented techniques, then opt for the TelerikForm component - it renders all those mentioned CSS classes automatically for you. We aim for simplicity and refrain from using multiple components in our feature demos. That's why the Window demo uses raw HTML instead of a TelerikForm.
