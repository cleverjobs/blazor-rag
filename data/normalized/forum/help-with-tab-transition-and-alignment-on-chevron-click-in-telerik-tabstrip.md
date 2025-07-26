# Help with Tab Transition and Alignment on Chevron Click in Telerik TabStrip

## Question

**JoeJoe** asked on 02 Apr 2025

Hi everyone, I'm working with the Telerik TabStrip component and need help with two issues: Tab Transition on Button Click: When I click the chevron buttons to navigate through the tabs, I want the visible tabs to change with a smooth transition effect. However, I'm having trouble applying a transition effect for this behavior. Can anyone provide guidance or an example of how to implement a transition when the visible tabs change? Aligning Tabs on Button Click: When I press the chevron buttons, I want the active tab to remain the same, but the newly visible left-most tab should be aligned at the start (left side) of the TabStrip. How can I ensure that after clicking a chevron, the newly displayed tabs are aligned to the start of the TabStrip? Any suggestions or code snippets that could help resolve these issues would be greatly appreciated! Thanks in advance!

### Response

**Nadezhda Tacheva** commented on 07 Apr 2025

Hi Joe, As Anislav correctly mentioned, the TabStrip does not provide the desired functionality out of the box. In terms of tab transition, I believe you can achieve that with CSS. As for the aligning tabs, I want to confirm if I properly understand what is your desired behavior and what problem you are trying to solve. By the current design, when the user presses the chevron buttons, the tab headers are scrolled but it is not guaranteed that all headers will be completely visible, some of them may be truncated. For example, in this demo, if I press the right scroll button, I may end up with the "London" and "Barcelona" tab headers not fully visible: Is this the scenario you want to cover? As I understand, you want to ensure that when the user presses the scroll buttons, the tab headers will always "snap to place" so the whole headers will be visible. Please let me know if I am missing something.

## Answer

**Anislav** answered on 05 Apr 2025

Hi Joe, The TabStrip component does not offer built-in support for these specific customizations. If these features are essential for your project, you may need to implement a custom tab componen from scratch to achieve the desired behavior. Regards, Anislav Atanasov
