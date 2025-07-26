# C# 8 features

## Question

**Bil** asked on 18 Mar 2020

Looking at your components for the first time and downloaded the 30 day trial today. I note in Visual Studio 2019 that you set <LangVersion> to 7.3 for each of the samples and the VS templates I've installed. Is this a requirement to stay compatible with your package? The big pull for us with C# 8 is nullable reference types. I suppose I can just turn it on and wait for Telerik components to be incompatible.

## Answer

**Marin Bratanov** answered on 19 Mar 2020

Hello Bill, There shouldn't be issues with using 8.0 (or removing this flag). We re not using such features at the moment, but they should work. The 7.3 version is a remnant from old MS templates that I have forgotten to remove from our templates, you should be able to remove it and have things working. In fact, we may also start using 8.0 features with our next release. Regards, Marin Bratanov
