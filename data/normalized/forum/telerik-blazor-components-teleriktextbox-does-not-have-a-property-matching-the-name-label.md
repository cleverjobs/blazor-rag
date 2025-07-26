# Telerik.Blazor.Components.TelerikTextBox' does not have a property matching the name 'Label'

## Question

**Rol** asked on 19 Jan 2022

Just upgraded to Telerik UI for Blazor 3.0. The Label property is removed from TelerikTextBox? This worked in version 2.30.

## Answer

**Joana** answered on 20 Jan 2022

Hi Roland, We removed the `Label` parameter in our 3.0.0 release. We will release a standalone FloatingLabel component in our 3.2.0. So, keeping the Label parameter would result in a conflict with the upcoming component. In addition, the Label in the textbox components had multiple issues and inconsistencies in our textbox components in terms of difference in size and styling. However, in order to provide migration path to our customers we have uploaded a KB that shows how to add such floating label: [https://docs.telerik.com/blazor-ui/knowledge-base/inputs-floating-label](https://docs.telerik.com/blazor-ui/knowledge-base/inputs-floating-label) I hope that the above solution will work on your case, and you can go through our documentation article that covers all breaking changes in our 3.0.0 release: [https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/3-0-0](https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/3-0-0) Regards, Joana

### Response

**Shannon** commented on 20 Jan 2022

What would've been cool would be not making this change until the FloatingLabel was ready. Then it would've been fairly quick and easy to update all the TextBoxes in a project. Instead I just spent all morning updating 300 textboxes and I know I will have to do it again once you release the FloatingLabel. That's not cool.

### Response

**Joana** commented on 25 Jan 2022

Hi Shannon, Thank you for the feedback. I definitely agree that the best approach when removing a feature is to provide the built-in alternative at the same time. We do try to follow this practice. I hope you understand that we put great effort in our major release and we did our best to implement all breaking changes that were prerequisite to highly demanded features by our customers. Thus, we needed to prioritize our backlog. We evaluated the issues related to the Label parameter along with its usage, reviewed the code quality, and then we made the hard choice to remove it with a KB how to achieve the same behavior, in favour of other important features. However, I appreciate your feedback and I hear your struggles while migrating your project. I assure you that we take our lessons and listen to our customers to adapt our workflows to fit to their needs.

### Response

**Shannon** commented on 25 Jan 2022

I totally understand. I am very happy with the latest release. It is really great. This was just a little thorn on the rose.

### Response

**Marko** commented on 27 Jan 2022

while you might understand them.. i don't. I've never had to place and manage a simple Label for a text field.... especially with this much code. In business world nobody cares about floating labels..... we need simple text field labels on top or on left/right with minimum coding! I don't see how a fancy/confusing floating label can remove such a standard feature.. sure.. easier for Telerik to implement and maintain.. but A LOT of work for us developers to implement and maintain hundreds of labels across business apps..... terrible decision worth of firing people.

### Response

**Joana** commented on 01 Feb 2022

Hi Marko, I understand your frustration. However, every coin has two sides and let me share more details on the matter. We try to keep the component API and architecture clean and flexible. This code style enables us to provide more features to our customers and they are able to customize the components, and additionally they have easier getting started experience with our source code. A good architecture suggests small units of components and easy to navigate html rendering. For instance, if an input element implement a label that can be positioned top and left, or has floating capabilities, it would bring more html elements and complexity that comes with a higher rendering cost. Moreover, the Label parameter was present only in our text components that brought inconsistencies to the projects of our customers as well. They needed to define external labels for all other numeric, bool, date editors and for a great amount of our customers this meant not using the Label parameter for the others as well. Based on your comment, I think we have potential actions that we might address and I would greatly appreciate the collaboration. I see that your demand is to have an easy label association with an input component aside from the FloatingLabel. I am adding my thoughts below about components that might fit to this requirement while keeping the input elements clean. Label Component Releasing a simple component that will render `<label>` element and will be able to wrap the input, or to be used outside of the component. FormField Component Currently, we have our Form component that automatically generates label and input editors based on the type for our customers. However, we might introduce a standalone FormField component that will: - automatically associate a label to the input label - support positioning of the label - support automatic generation of the input element - support template for defining custom label/editor I hope that the above information and suggested approaches make sense to you.

### Response

**Brian** commented on 07 Feb 2022

Also very frustrated with this and a bit surprised Progress isn't already walking this back. This thread did not help much - I am sure you have good reasons, but it seems like you are ignoring what your customers are telling you. Any moment where I have to touch hundreds of text boxes, knowing I will have to do it again soon, which feels like a strong indicator that you think this is acceptable and are out of touch with the reality on the ground, is a moment where my team will have to take a look at the competition and re-evaluate who will be better to work with long term. After all, you already have us doing days of pointless work. Maybe that time is better spent migrating. I would think you would want to avoid moments like this.

### Response

**Joana** commented on 10 Feb 2022

Hello Bryan, I am sorry to hear that it took days to migrate to the change. It seems that we underestimated the cost of the effort for our customers. It depends on every case, however, we thought that the migration would be a quick replacement. For reference, we assumed that the change would come down to a regex replacement of all occurences. One more possible alternative is to wrap the component that would require only a change of occurences of `TelerikTextBox` to `TelerikLabelText` like in the following example I created: [https://blazorrepl.telerik.com/mwYGPuvU01nmbOVQ16](https://blazorrepl.telerik.com/mwYGPuvU01nmbOVQ16) Based on the feedback we gathered in this thread, we are currently re-prioritizing and evaluating the option for earlier release date of the Floating Label component.

### Response

**Brian** commented on 10 Feb 2022

Thanks for the reply. The regex path occurred to me, but the wrapper would probably work a little better given that this is going to change again soon. Kind of clunky to have that as part of our architecture forever - I guess we could consider unwinding it once the floating label is available.

### Response

**Marko** commented on 15 Feb 2022

hi Joana, i know it is just my opinion and i know others might have different use cases, but no matter how i look at it i still don't see any sense in the decision to strip the label out of the component. You mention " A good architecture suggests small units of components and easy to navigate " and i agree, but this also applies for our code. And those "small units of components" are possible by using a component suite, such as Telerik UI for Blazor, which hide most of complexity from the developers. So the component vendors should not shy away from tackling heavier tasks and hide behind complexity or performance reasons.. In this case, and i'm sure a lot of teams will be forced to do the same, we will need to implement similar "TelerikLabelText" wrapper for all form components - which should save us a lot of unnecessary coding. In the end it will be the same as if you would keep the label already in the field except that now it will really impact rendering cost and complexity... Other option is to look at the source and see if we can fix it there. But no matter how many solutions or workarounds you present it will still be something which will add to our development time which is the opposite to what a good component should do. But as mentioned, just one opinion of many, and you have already made a decision, so we need to live with it and move on.

### Response

**Brian** commented on 15 Feb 2022

@Marko I actually do not see much stopping them from adding the label property back in. It is probably a little ugly in their internal architecture... But why would I care about that?

### Response

**Joana** commented on 15 Feb 2022

Hello Marko, Thank you so much for the feedback. Absolutely, the goal and mission of our components is to save our customers time through clean and easy setup. We managed to prioritize the Floating Label component, and started working on it right away. It is currently in design stage, however, the configuration should be similar to the following snippet: <TelerikFloatingLabel Text="Label"> <TelerikTextBox Id="txt"...> </TelerikTextBox> </TelerikFloatingLabel> The workarounds were a suggestion to facilitate the transition until we release the FloatingLabel. However, we hope that the new Floating Label component will fit to the requirements of all projects as it will work with all input-based components and pickers, not only with the TextBox, TextArea. MaskedTextBox components.

### Response

**Marko** commented on 17 Feb 2022

hi Joana, thank you very much for your effort in this issue and please note that the overall feeling with the component set is very good and i love the progress that was done over the past year and the roadmap as well. Can you please just elaborate why the component will be named TelerikFloatingLabel? I would expect it to be named TelerikLabel and we could use it to display top or left/right label, with or without floating by using a parent css class or form property which is there already and/or specific setting on a field. Or will there be two components? Will there be a need to manage the Id between Label and TextBox? This is something that greatly affect the readability of the code when there are a lot of fields on the form and you need to come up with unique id names.

### Response

**Joana** commented on 22 Feb 2022

Hi Marko, The goal of the component is to fill the gap of the removed Label parameter of the TextBox components. Thus, it will have fly out behavior to match the same user experience, but customers will be able to use it with all our input-based components. The floating label component will automatically associate the label with the id of the telerik input component. This is an important feature to assure accessibility, and it will be built-in so that our customers would not need additional configuration. Regarding the idea for TelerikLabel component, I definitely see value in it and I have generated a feature request from this support thread. [https://feedback.telerik.com/blazor/1554821](https://feedback.telerik.com/blazor/1554821) We can also prioritize this component based on the feedback. However, our fist step with the FloatingLabel is to assure that we provide easy migration since the removal of the label parameter for textbox components.
