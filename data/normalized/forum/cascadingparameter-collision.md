# CascadingParameter collision?

## Question

**Mar** asked on 31 Mar 2021

The new Dialog component is passed as a cascading parameter. Is there a way to name the parameter to prevent collisions with out cascading parameters?

## Answer

**Matthias** answered on 06 Apr 2021

This works: [CascadingParameter] public DialogFactory myDialog { get; set; }

### Response

**Marc Simkin** answered on 06 Apr 2021

It should work. The issue, if you already have another cascading parameter that is not named. It is just bad form for Telerik to relay on being the only unnamed cascading parameter.

### Response

**Matthias** answered on 06 Apr 2021

I have to use two cascading parameters and have no problems: [CascadingParameter] public DialogFactory Dialogs { get; set; } [CascadingParameter] private string ip { get; set; }

### Response

**Marin Bratanov** answered on 06 Apr 2021

Hello Marc, We are not aware of problems with that and what Matthias said should be the case. If you are still having issues with that, I recommend you isolate the Telerik problem to a small sample and send it to us in a support ticket so we can review it. Regards, Marin Bratanov
