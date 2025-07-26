# Password char?

## Question

**Ran** asked on 16 Aug 2019

Is there a way to set a password char on the blazor textbox? Thanks ... Ed

## Answer

**Marin Bratanov** answered on 16 Aug 2019

Hello Ed, At the moment, there isn't a way to do this. Perhaps it will be implemented through arbitrary attributes so you could set type=password on the <input /> element directly. You can follow these ideas in the following pages (I've already added your vote): [https://feedback.telerik.com/blazor/1416922-add-to-teleriktextbox-more-parameters-such-as-type-autocomplete-required-readonly](https://feedback.telerik.com/blazor/1416922-add-to-teleriktextbox-more-parameters-such-as-type-autocomplete-required-readonly) and [https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes.](https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes.) Regards, Marin Bratanov

### Response

**James** answered on 03 Sep 2019

Hi Marin, I was just about to request this feature but see it's been in the queue for a while now, do you know if there is any plan now to implement types onto your inputs? Having a textbox or numeric textbox that can have a password type, would render the text as bullets, and maybe having an eye icon to toggle text and password would be ideal.

### Response

**Marin Bratanov** answered on 03 Sep 2019

Hello James, The UI for Blazor suite is very young (just like the technology stack), and we need to focus first on the components with heavy impact (mostly, the grid and the various editors it requires). You can find our rough plans in our roadmap: [https://www.telerik.com/support/whats-new/blazor-ui/roadmap.](https://www.telerik.com/support/whats-new/blazor-ui/roadmap.) At the time of writing, the menu, grid grouping and grid selection, and the time picker are done. The thing about types of input is that perhaps the attribute splatting feature will make it unnecessary to implement separate components for passwords. On the other hand, features like the "eye" button may require separate components, or features in existing ones. Also have dedicated date/time/numerical inputs, so maybe it will make sense to have a password one. Attribute splatting itself is something we still need to consider carefully, because complex structures like our components are not clearly defined like the MS docs for a single input. This is where the way the framework goes in general, and the feedback of the community are important - once we know whether people would rather use the regular textbox and add a type attribute to it, or have a separate component, we can go in that direction. Having that feedback recorded will also let us gauge the community interest and prioritize the tasks. In summary, I'd encourage you to leave your votes and comments in the

### Response

**Jame** answered on 04 Sep 2019

Okay awesome, thanks for the reply Marin!

### Response

**Marin Bratanov** answered on 05 Sep 2019

You're welcome. I wouold encourage you to post your feedback and preferences regarding passwords in the

### Response

**SBSDEV** answered on 20 Feb 2020

Marin, Adding an InputType parameter (with default="text") and adding it to the RenderTree in the TelerikTextBox class would be very easy and save a lot of hassle. [Parameter] public string InputType { get; set; }="text"; Then: __builder.AddAttribute(7, "type", this.InputType); Please how can we ask to have dev add this 5 minute change (another few minutes to document it)? Thank you!

### Response

**Marin Bratanov** answered on 20 Feb 2020

Hi Craig, While a single attribute would be quick, there is a more important concern here - unified experience for all components, and choosing the correct approach (future proofing) so we don't have to do a breaking change in this regard. That is, I would invite you to join the discussion on arbitrary attributes and attribute splatting, with the concept that we need to look for consistency (like - how should this work for a grid or other complex component) and to also not open the door for problems (like attributes that can break something like data-id which we use, or adding a type=number to an input that needs to get text input): [https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes.](https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes.) If you would prefer the approach where those attributes come from explicit parameters, add your Vote for this one: [https://feedback.telerik.com/blazor/1416922-add-to-teleriktextbox-more-parameters-such-as-type-autocomplete-required-readonly.](https://feedback.telerik.com/blazor/1416922-add-to-teleriktextbox-more-parameters-such-as-type-autocomplete-required-readonly.) I would appreciate any feedback you may have on either approach - either here, or in the respective portal page. For the time being, you could use a regular <input> with our class for appearance: [https://docs.telerik.com/blazor-ui/themes/form-elements#inputs](https://docs.telerik.com/blazor-ui/themes/form-elements#inputs) Regards, Marin Bratanov

### Response

**SBSDEV** answered on 01 Mar 2020

Hi Marin, I appreciate your thoughtful reply. I think that both explicit parameters for common attributes (I upvoted 1416922) and some type of extensibility to pass through other attributes as needed as a last line of defense would be useful and would not be a breaking change. Ultimately I imagine the roadmap includes things like enhanced Intellisense in the editing experience so explicit params lend itself to a better dev experience and give more visibility to the customization possibilities specific to each type of control. Thank you again.

### Response

**Marin Bratanov** answered on 02 Mar 2020

Thank you for your feedback, Craig. At this point, it looks like explicit attributes will be more useful and are the preferred way for most people, so I am inclined to recommend implementing that. Whether a fallback for attribute splatting will be implemented is still to be determined, because we haven't seen any use cases for that beyond the few standard input attributes (type, inputtype, autocomplete...). Regards, Marin Bratanov
