# MinLength, MaxLength, Pattern

## Question

**Pau** asked on 20 Sep 2019

Is it just me or were these properties removed from the TextBox? I had code with those properties set that no longer compiles after upgrading.

## Answer

**Marin Bratanov** answered on 22 Sep 2019

Hi Paul, Yes, these parameters have been removed. You can find the full list of breaking changes in 2.0.0 in the following page: [https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/2-0-0.](https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/2-0-0.) Those parameters used to render as HTML attributes which is not very effective. For one, minlength is still not supported well by the browsers, so it wouldn't really work. Then, such things are better left to validation so a meaningful message can be shown to the user as to why their input is not being accepted. Thirdly, it is likely that they will be brought back through attribute splatting. Also, you can respond to events of the textbox and if input does not fit your needs, you can avoid updating it in the model, in case validation is not an option. Regards, Marin Bratanov

### Response

**Chris** commented on 28 Jul 2021

Based on other posts here, attribute splatting was not introduced. How you do recommend implementing maxlength?

### Response

**Marin Bratanov** commented on 28 Jul 2021

Indeed, Chris, attribute splatting is not implemented because it is far too ambiguous for most components. To implement max length, I recommend one (or both) of the following options: validation using the ValueChanged event and not updating the view-model field if the new value does not match your criteria
