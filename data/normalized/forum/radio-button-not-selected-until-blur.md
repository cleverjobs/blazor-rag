# Radio button not selected until blur

## Question

**Mat** asked on 05 Aug 2021

When I select an option in a radio group, the selection is focused (I can see the styled highlighting) but not selected. When the radio group is blurred (loses focus), the selected item now appears selected. Figure: Item selected and programmatic selection successful, but radio button is not checked Figure: Once I click out of the radio group, the selected button is checked

### Response

**Dimo** commented on 09 Aug 2021

Hi Matt, I tried to reproduce the described faulty behavior on our online RadioGroup demos and on a standalone local test page, which uses the sample snippet from our RadioGroup documentation. I used Win/Chrome and Mac/Safari. In all cases, the "selected" styles were applied as expected. Since other people report the issue too, it seems there is something wrong here. Can you provide a test page that exhibits the described problem and we will review it immediately? Thanks!

### Response

**Josh** commented on 10 Aug 2021

We have had this problem when using Tailwind's tailwind-forms module, with Telerik for Blazor UI. Tailwind does a reset and has a comprehensive set of attribute-based pseudo-styles by default. Telerik's styles are overridden if Tailwind's are loaded later. In most apps, Tailwind would load after Telerik in order to allow the application to do overrides. As a short-term fix, Tailwind forms has a class-based strategy that increases its specificity. tailwindcss-forms#using-classes-instead-of-element-selectors describes how to resolve - if you're using Tailwind. But ideally, Telerik's styles would be slightly more specific and have safe defaults under their own class namespace, so that other styling - whether from Tailwind or something else - targeting type attributes isn't more specific than the k-checkbox selectors. This wouldn't stop applications from explicitly styling k-checkbox or radio if required, but would require them to be more specific than a basic [type] selector. I have simulated the problem in a fiddle here: JSFiddle - Code Playground Test 1 fails: Test 2 passes: But test 2 is an unlikely use scenario I think, because typically app users will want their app CSS to come last to allow overrides. This means we need a 3rd case: In this case, we join the classnames with attribute selectors. There might be a more effective way to do this just on the base class, rather than the state classes.

### Response

**Dimo** commented on 10 Aug 2021

Hi Josh, Thanks a lot for the detailed description of your use case and JSFiddle. This is a tricky situation. Theoretically, we can increase the specificity of our selectors, but this can have various implications, for example - Our CSS will become more complex, larger and cumbersome to maintain. It will become even more cumbersome to override by our customers. If we increase the specificity of our styles, we will break all customers that already have some overrides of their own. We will invest time and effort to unofficially start supporting third-party libraries that we actually do not. Tailwind is using type selectors, so they obviously do not expect to be used together with other libraries that apply styles. If we decide to "fix" their approach in our CSS, this creates some sort of a principle dilemma. I hope this makes sense.

## Answer

**Baires** answered on 05 Aug 2021

Same here, seems like something related to the latest release, also some styles broken after that here
