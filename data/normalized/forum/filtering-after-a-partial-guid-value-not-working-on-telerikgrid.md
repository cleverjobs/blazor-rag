# Filtering after a partial Guid value not working on TelerikGrid

## Question

**Tad** asked on 08 May 2024

We are using a TelerikGrid which allows to filter various properties. One of our properties is a name of Id, which is of Guid type. Of course when we give a full Guid Id into the filter, the filter works, but as soon as we put a partial Guid value the filter breaks, because as expected, it cannot parse the given value. Error: System.FormatException: Unrecognized Guid format. at System.Guid.GuidResult.SetFailure(ParseFailure failureKind) at System.Guid.TryParseGuid(ReadOnlySpan`1 guidString, GuidResult& result) at System.Guid..ctor(String g) We have tried to convert guid value into string and then pass it into the filter, but it expects a Guid data type. Is there a way to internally let the guid filter know, that he should expect a string value instead of Guid? Filtering after Guid doesn't really make sense, since user will most of the time just type a part of the full guid Id value. Thank you for assistence!

## Answer

**Dimo** answered on 13 May 2024

Hello Tadas, The only data type, which supports a "contains" filtering is the string. So, you have two options: Change the type of the Id property to string and call ToString () when creating new Guid values. Bind the Grid with an OnRead event handler and implement custom filtering on your own without using ToDataSourceResult(). I don't think this option makes sense, because it's a lot more work than the previous one. Regards, Dimo Progress Telerik
