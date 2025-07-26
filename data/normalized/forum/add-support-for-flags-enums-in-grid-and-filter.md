# Add support for [Flags] enums in Grid and Filter

## Question

**Pin** asked on 15 Aug 2022

Hey, I don't see any real way to support enums with the [Flags] attribute for Grid and Filter. The display in the grid column is fine, but the filter menu is useless as it only does a straight up comparison to single values. It would be great if the filter on the grid (and the filter component) had an option for HasFlags, where you can select a value to compare for it.

## Answer

**Nadezhda Tacheva** answered on 18 Aug 2022

Hi Matthew, You are correct, such a use case is not supported out of the box for the Grid filtering or the Filter component. They need to be adjusted to deliver the desired result. I will now share tips for the two components as follows: Grid To override the default behavior of the Grid filtering, you may use a Filter Menu Template. You can include a set of checkboxes for the available enum value, so the user can select multiple values to filter by. In case you want to allow the user select a specific operator to combine the values by (AND/OR, for example), you may also include a dropdown with the desired options in the template. You should create a FilterDescriptor for each of the enum values and combine the filter descriptors as needed according to the selected operator. When checkboxes are selected, you can add the corresponding FilterDescriptors in a CompositeFilterDescriptor for example and use it to filter the Grid. The business logic handling the filtering would very much depend on the exact scenario you are trying to achieve and how you want to combine the enum options. Examples of creating a custom filter menu you can find in the above linked article for Filter Menu Template and in this demo. FIlter Currently, the Filter component does not allow similar customization of its Filter Field. However, we will expose a Filter Field Template in a future version of the component. Once available, it will allow you control the default behavior of the Filter Field. I hope you will find the above information useful. If any further questions appear in the process, please let us know. Regards, Nadezhda Tacheva

### Response

**Pingu** commented on 20 Aug 2022

Hi Nadezhda, I'm still not convinced that its possible to do this with the Grid Filter... We need to create a FilterDescriptor, which requires a FilterOperator. There are no acceptable values for FilterOperator that you could use to effectively compare a flags enum. If you have an enum such as: enum MyEnum
{
Val1=0,
Val2=1 <<0,
Val3=1 <<1,
Val4=1 <<2,
Val5=1 <<3,
Val6=1 <<4 } then lets say you have something with a value of MyEnum.Val2 | MyEnum.Val3. How would you compare against that? The value returned, numericly, is 3. But the comparison when filtering for Val2 or for Val3 individually would be a comparison with values 1 or 2. You can only really do this comparison with the HasFlag operation (or bitwise operators), but there is no way to create a FilterDescriptor to compare things using any bitwise operators.

### Response

**Nadezhda Tacheva** commented on 24 Aug 2022

Hi Matthew, I will need some more time to additionally revise this use case with the team. I will get back to you to suggest the best option to proceed. Thank you for your patience in the meantime!

### Response

**Nadezhda Tacheva** answered on 29 Aug 2022

Hi Matthew, Thank you for your patience once again! I am stepping in to provide further guidance on how to proceed. To filter the Grid by multiple enum values, you will need to create filter descriptor where the value should be matching the combination of the selected enum values. If you also want to allow filtering by single enum values, you can create separate filter descriptors for the single values as well. I am hereby including an example to better illustrate the approach: [https://blazorrepl.telerik.com/QQkCwNEg29eGDakw49.](https://blazorrepl.telerik.com/QQkCwNEg29eGDakw49.) Click the button to filter the Grid by size XS or S, or their combination. You may notice how the CompositeFilterDescriptor that the filter menu uses has a collection of three FilterDescriptor instances - one for size XS (value=1), one for size S (value=2) and one for their combined values (value=3). The LogicalOperator is OR, so the displayed values will include records with single sizes S and XS, and records that contain both these sizes. In this sample the Grid is programmatically filtered for example purposes. In your scenario, you may handle the ValueChanged event of the checkboxes to create the corresponding descriptors. I hope the above tips and example will help you move forward with the implementation on your side. Regards, Nadezhda Tacheva

### Response

**Pingu** commented on 29 Aug 2022

Hi, Thanks for the answer. The example you provided doesn't seem to work all that well? To set the filter you need to clear it first, even though it doesn't appear to be filtered yet, and then when you filter, for example, for size Large only, the results it returns doesn't match that at all. Also the checkboxes default back to XS and S every time too. Also, I feel like tackling things in the way the example attempts to is only tackling the problem if you have all of the data readily available, but not a good solution for when a grid is using OnRead to get results...

### Response

**Nadezhda Tacheva** commented on 01 Sep 2022

Hi Matthew, The linked sample is just a basic example which focuses on the type of filter descriptors you will need to achieve your desired result. It serves as a guidance to move forward rather than providing complete implementation of the desired scenario. The sample showcases programmatic filtering of the Grid by sizes XS and S, and their combination. The checkboxes for XS and S are programmatically checked for example purposes. Filtering by L size is not going to deliver the desired result since it is not implemented. Additionally, let me provide some clarification when handling the OnRead event. The listed approach suggests handling the ValueChanged of the CheckBoxes in the FilterMenuTemplate to create the needed filter descriptors in the context. That said, by the time the OnRead event handler is raised, the corresponding filter descriptors will already be added to the Grid and present in the Request.Filters of the event arguments. Thus, you can get the relevant data based on the applied filters. I hope the above details will bring more clarification on the scenario. In case you are facing any other difficulties with incorporating the approach on your side, I can put you in touch with our Professional Services team who can assist with such complete implementations. Please let me know if you'd like to proceed with that option.
