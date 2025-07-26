# Changing look of the Wizard

## Question

**Pau** asked on 01 Jun 2022

Hi Before we started with Telerik our design office created this wizard style. Questions: 1. can we alter the look of the Wizard? (CSS?) 2. the Wizard should have the same size for each step 3. can we change the color of the buttons? Thanks for answering! Eric

### Response

**Dimo** commented on 03 Jun 2022

@Eric - for any CSS customizations on our components, see articles How to override theme styles and Blazor theme customization options. In general, a lot of customizations are possible, as long as the component's HTML markup is compatible with the desired look. For same-size steps, I assume you are talking about the Wizard step containers, and not the Stepper steps at the top. In this case, use a fixed-height container inside each step's <Content> tag.

### Response

**Paul** commented on 24 Oct 2022

Which container is preferable?

### Response

**Dimo** commented on 24 Oct 2022

@Paul - I would use a <div>, because it can contain any other HTML element.
