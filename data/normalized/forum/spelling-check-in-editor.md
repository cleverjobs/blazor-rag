# Spelling Check in Editor

## Question

**Mat** asked on 08 Jul 2021

Is there a plan to include Spellchecker in Blazor Editor? We have some spelling-challenged users that have specifically requested this functionality. Or will we need to add it as a Custom Tool?

## Answer

**Marin Bratanov** answered on 08 Jul 2021

Hello Matt, The editor lets the browser do the spellchecking which lets each user have their own language and customized dictionaries. Nowadays those spellcheckers are rather good, and all modern browsers have them. Thus, we do not plan to provide an explicit tool for this like we had in WebForms 20 years ago (and still do because we can't just remove features). If you need something more advanced or different than what browsers offer, a custom tool is a great solution. You may also want to Vote for and Follow the implementation of this feature that could allow you to plug into the underlying editing engine with JS: [https://feedback.telerik.com/blazor/1492857-expose-a-way-to-write-custom-plugins-for-the-underlying-prosemirror-engine](https://feedback.telerik.com/blazor/1492857-expose-a-way-to-write-custom-plugins-for-the-underlying-prosemirror-engine) Regards, Marin Bratanov

### Response

**Matt** commented on 08 Jul 2021

As usual, thank you for the quick response. My team all felt the browser spell checkers would be the *obvious* solution because that is what we would do. However, our page is for our field workers who generally are less tech savvy...and horrible spellers, thus we try to make their data work more efficient. There are a couple of NuGet options out there we might try. But we may have to guide them a little harder in the direction of the browser functionality.
