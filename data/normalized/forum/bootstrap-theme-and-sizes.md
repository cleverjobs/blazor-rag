# Bootstrap theme and sizes

## Question

**Jas** asked on 13 May 2021

I switched Telerik to the Bootstrap theme, which at first looked good, but realized all the Telerik controls don't really seem to be using Bootstrap and are set to the default sizes. I need the small (sm) sizes which in Bootstrap is trivial to change. Is there a better way to make all the controls smaller? I've found some controls will accept Bootstrap css while others will not making using Telerik time consuming. The best way I've found to make the Grid smaller is to make my own CSS classes and extensive use of the !important tag, but I still have a lot of work left to get the Grid sized appropriately. Other controls are inconsistent. For example, this works: <TelerikTextBox ... Class="form-control form-control-sm" /> But this does not: <TelerikNumericTextBox ... Class="form-control form-control-sm" />

### Response

**Sanjay** commented on 11 Mar 2025

You're having trouble consistently sizing Telerik controls with Bootstrap. It's often easier and more reliable to use a complete Bootstrap template or component library instead of trying to force Bootstrap onto Telerik. This will give you consistent sizing and save you time.

## Answer

**Dimo** answered on 14 May 2021

Hello Jason, The main idea of the our Bootstrap theme is to provide consistent color scheme for our components with the Bootstrap CSS framework. Normally, our components do not render Bootstrap CSS classes, but they may "automagically" obey some Bootstrap framework styles. This will depend on the use case, component HTML markup and CSS specificity of all involved styles from both products. Such compatibility, however, is not universally claimed. Some notes on the Bootstrap theme are available at: [https://docs.telerik.com/blazor-ui/themes/overview#bootstrap-notes](https://docs.telerik.com/blazor-ui/themes/overview#bootstrap-notes) Regarding form-control-sm, I created a test page and both the TelerikTextBox and TelerikNumericTextBox applied smaller padding and height styles as expected. The only issue is with the font-size, which remained 1rem. You can workaround this with a couple of additional CSS rules: .form-control-sm.k-textbox,.form-control-sm.k-input { font-size: . 875rem;
}.form-control-lg.k-textbox,.form-control-lg.k-input { font-size: 1.25rem;
} The resulting appearance should be: Future plans: Note that in future UI for Blazor / Kendo UI versions, the same end result will require a different approach. We will introduce sizing API and our own "small" and "large" classes that our components will use to control their sizing. Our input components have more complex HTML rendering than plain textboxes. We prefer to avoid the need to rely on third-party classes and styles to tweak our product appearance. Regards, Dimo

### Response

**Jason** commented on 14 May 2021

Thanks for the completeness of your answer. That helps get me pointed in the right direction. The TelerikNumericTextBox is still a few pixels taller than the other text boxes though, so I am finding that I'm spending a lot of time with the CSS anytime I choose a Telerik control over standard html. The frustration for me is the whole reason I'm using Bootstrap is so I don't have to spend as much time creating custom CSS, and the reason we're using Telerik is to save time, not add time.

### Response

**Dimo** commented on 14 May 2021

I understand your concern. It is not trivial to ensure pixel-perfect compatibility with third-party library styles, that's why we will try to make the job of developers simpler and easier with the new sizing mechanism that we will introduce.
