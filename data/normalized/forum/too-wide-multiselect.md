# Too wide MultiSelect

## Question

**Rol** asked on 31 Jul 2020

The MultiSelect needlesly bumps up the width when 2 chips don't fit on the same line. After the wrap the width stays too large. See the attached image.

## Answer

**Roland** answered on 31 Jul 2020

and this fixes it for me: .k-multiselect-wrap.k-floatwrap { inline-size: min-content; min-width: 100%; }

### Response

**Marin Bratanov** answered on 31 Jul 2020

Hi Roland, On my end the width does not change from what was defined. Could you compare against the sample I am attaching and see what is the difference causing the issue? Can you reproduce it on this sample? Regards, Marin Bratanov

### Response

**Roland** answered on 31 Jul 2020

Your example works as expected, so it must be something in the styles I use. Not going to spend any time on it now, because I have my workaround.
