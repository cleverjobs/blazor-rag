# Is it possible to remove this gap when drawing an area & line series to the same chart?

## Question

**Mar** asked on 19 Dec 2023

Hi When we plot an area series on the same chart as a line series we find that the area series no longer fills the full width of the chart, as shown below. Here is a REPL with the code to reproduce it. Is there a way to restore the behaviour of the area series, like this? Thank you Mark

## Answer

**Hristian Stefanov** answered on 22 Dec 2023

Hi Mark, I'm pasting here the answer I gave you in the public feature request item so the forum community can benefit from it.=======The way the area series acts in combination with the line series is influenced by the line series, which centers the categories within each sector. Consequently, the area series aligns itself accordingly. To address this, we have a separate feature request: Add the justified configuration for the Chart. Once implemented, you will gain the flexibility to fine-tune category positioning with line series configuration, eliminating any space at the beginning and end of the area series. I voted there on your behalf.=======Regards, Hristian Stefanov Progress Telerik
