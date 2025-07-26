# Deserialize CompositeFilterDescriptor

## Question

**Joh** asked on 11 Jul 2022

I'm trying to save the CompositeFilterDescriptor. If I do the following: var serializedFilter=JsonSerializer.Serialize(FilterValue); var deserializedFilter=JsonSerializer.Deserialize<CompositeFilterDescriptor>(serializedFilter); The deserializedFilter FilterDescriptor.MemberType is null and if used causes the the display of the filters to throw an exception. Note that the filters are part of a user preferences class that is serialized as a whole. So is there a proper way to serialize/deserialize?

## Answer

**Dimo** answered on 14 Jul 2022

Hi John, MemberType is a Type and falls under a known limitation. You can either populate the MemberTypes manually after deserialization, or implement some more elaborate workaround that will automate the process for you. Regards, Dimo

### Response

**Víctor** commented on 09 Mar 2023

I would also like to deserialize it. Do you have an example? I want to create filter pressets, I don't understend how I cold do that if I can not deserialize the filters. I see there is a .ToJson() method, why not just add a FromJson method?

### Response

**Dimo** commented on 09 Mar 2023

@Victor - you can serialize and deserialize filters like any other object. The only thing to do after deserialization is to set the MemberType property of each FilterDescriptor manually. Since you know the Member property values, you should be able to find out and set the correct MemberType as well.
