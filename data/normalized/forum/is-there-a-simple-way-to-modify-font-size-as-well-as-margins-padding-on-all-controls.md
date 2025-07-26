# Is there a simple way to modify font size as well as margins/padding on all controls

## Question

**Jef** asked on 06 Jan 2021

I'm finding the default font size as well as the overall amount of white space around the controls to be a bit much. I'm trying to produce a much more condensed interface with a smaller font and less margins/padding. I've been inspecting all of the rendered UI elements in an attempt to figure out the most efficient way to accomplish this but my head is spinning. So far my assessment is that I'm going to have to do this one component at a time. And even with that approach I'm struggling. For example, I've reduced the font size to 12px but the date picker remains the same size but with the smaller font. Not quite what I was going for. I feel I could spend weeks trying to figure out every single "k-" class that I will need to override. I was hoping the theme builder would allow me to pick a font size/family as well as options to adjust margins/padding around the elements but that doesn't seem to be the case. Any suggestions? Where am I going wrong?

## Answer

**Marin Bratanov** answered on 07 Jan 2021

Hi Jeffrey, We have it in our plans to review this, among a few other things, later this year. If/when improvements and new features become available they will be exposed accordingly - for example, documentation, or new features in the theme builder tool. I'm afraid I cannot provide more concrete information, because the detailed investigation must be completed first. Regards, Marin Bratanov

### Response

**Jeffrey** answered on 07 Jan 2021

Thanks Marin. I've actually made some good progress. I was able to address the date picker width by getting rid of the min-width on the k-calendar-header class. I've been fussing a bit with the box-shadow on the dropdown/popup. I tried the box-shadow on the k-animation-container class but I don't like how the shadow appears below the dropdown before animation has completed. I then tried an alternate solution with the box-shadow on the combination of "k-animation-contatiner k-popup" class but the shadow is hidden unless I set overflow:visible on the k-animation-container. But then that results in the dropdown fully appearing above the combobox before it then animates downward. I ended up with the alternate solution of this: .k-animation-container { padding: 7px; } I've still got an issue with the dropdown height not being quite right and cutting off the bottom of the list. Overriding the height on the k-animation-container fixes it but it also then messes up the calendar popup. I'm sure I'll figure it out.

### Response

**Marin Bratanov** answered on 07 Jan 2021

Hello Jeffrey, It's good to see you making headway! In our next release (planned at the end of the month) all components will have a Class parameter, and the dropdowns will also have a PopupClass - this will let you set custom CSS rules per component instance (such as min-height, max-height, min-width and max-width) to control their appearance. Regards, Marin Bratanov

### Response

**Jeffrey** answered on 07 Jan 2021

Glad to hear... eagerly awaiting the new release.
