# How do I format the <option> part of a dropdown?

## Question

**Rol** asked on 07 Sep 2020

See the attached image. The flag images are only 21px wide, but the PopupWidth is 69px. So I seem to have 48px of margins and/or paddding. Since the dropdown collapses when it no longer has the focus, i cannot see the styles in Chrome Devtools. I am using <ItemTemplate> and <ValueTemplate> to format the <select> and <option> elements.

## Answer

**Marin Bratanov** answered on 07 Sep 2020

Hello Roland, The following blog posts can help you examine elements, including popups that hide: general principles: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools) more advanced scenarios, including hiding popups: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools-(part-2)](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools-(part-2)) - see the Inspect Auto-Hiding Tooltips and Elements section The dropdown elements have some default padding that you can remove globally for all dropdowns. For particular instances, this needs to be implemented first: [https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance.](https://feedback.telerik.com/blazor/1433654-component-specific-css-classes-and-ability-to-set-classes-per-instance.) Here's a very basic example of removing all paddings from the dropdowns (note that it will affect other dropdowns on the page too): <style>.k-list-scroller.k-list li.k-item { padding: 0;
} </style> <TelerikDropDownList Data="@MyList" @bind-Value="@MyItem" PopupWidth="auto" PopupHeight="auto"> <ValueTemplate> @context </ValueTemplate> <ItemTemplate> @context </ItemTemplate> </TelerikDropDownList> @code {
protected List <string> MyList=new List <string> () { "a", "b", "c" };

protected string MyItem { get; set; }="b";
} Regards, Marin Bratanov
