# Can you make the Blazor ComboBox have a ValueTemplate and the DropDownList have a PlaceHolder?

## Question

**SLSL** asked on 19 Dec 2019

I need to have both the PlaceHolder and the ValueTemplate but it seems the ValueTemplate only exist on the DropDownList while the PlaceHolder only exist on the ComboBox. Is it possible to make it available for both controls so it is consistent? If not possible then have the ComboBox have the ValueTemplate. Thanks.

## Answer

**Marin Bratanov** answered on 20 Dec 2019

Hello, In the main element there is only room for one - either a placeholder, or a value template. Such features cannot co-exist. There is a key difference between the components: The dropdown list always has a selected value. This is why it offers a value template - there is always something to show there. Since the user chooses an item from a predefined list of options, you can render anything in the main element - it's just a <span>. The combo box does not always have a selected item and it can act as a regular textbox (allow free text input). This is why it offers a placeholder - there may be no item from its data source matching the user input so a value template would throw exceptions. So, the combo box is basically an <input> as its main element and it cannot hold arbitrary content. This difference in the nature, use case and user experience between the components provides the different feature sets. That said, you may want to vote for and follow the request for this change that will make setting the default text in the dropdown much easier: [https://feedback.telerik.com/blazor/1431968-defaultitem-is-split-into-defaultvalue-and-defaulttext-breaking-change.](https://feedback.telerik.com/blazor/1431968-defaultitem-is-split-into-defaultvalue-and-defaulttext-breaking-change.) You may also want to vote for and follow this feature on allowing a filtering feature in the dropdownlist: [https://feedback.telerik.com/blazor/1427877-filter-search-look-ahead.](https://feedback.telerik.com/blazor/1427877-filter-search-look-ahead.) That would let you have the value template and a filter textbox in the dropdown would let the users filter in a fashion similar to the combo box. That said on the current state of affairs, would you envision something else in terms of functionality? What is the goal of having both features in both components and how would their rendering and UX operate? Regards, Marin Bratanov

### Response

**SL** answered on 20 Dec 2019

I just thought that a ValueTemplate should be possible in the ComboBox as I'm able to do this using the standard html elements: <select id="program" class="custom-select" onchange="@ProgramChanged"> <option value="">-- Select Program --</option> @foreach (var item in programs) { <option class="@(item.Count !=0 ? "optionbold":null)" value="@item.ProgramCode">@item.ProgramCode - @item.Name </option> } </select>

### Response

**Marin Bratanov** answered on 20 Dec 2019

Hello, The standard select element is equivalent to the DropDownList component we have, it is not equivalent to the combo box, because you can't type a custom value in it. The "Select Program" placeholder item is used through the DefaultItem feature (see here ) that may soon be replaced by a string property (see here ). Thus, if you use a DropDownList component, you can have the same behavior, including the ValueTemplate that you don't really have in the standard <select>. Regards, Marin Bratanov

### Response

**SL** answered on 20 Dec 2019

Thank you. That is exactly what I'm looking for. I'm looking at the online demo and the combo/dropdown docs but did not look at the rest of the docs.
