# Metrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_type** | **str** | the type of user the metric was derived from. For example, a count derived from a &#x60;collaborative&#x60; is the number of employers in that collaborative, whereas a count derived from &#x60;pilot user&#x60; is the number of &#x60;pilot users&#x60; at that time (e.g. using a recomemendation) | [optional] 
**uuid** | **str** | If given, the matching uuid in the matchTable (a row in the matchTable) that this &#x60;scoredRecommendation&#x60; applies to (e.g. one of several &#x60;scoredRecommendation&#x60;s that could be assigned to a particular competency property in the json-ld file). If no uuid present and recommendation, then this applies to the entire converted job description (e.g., in general you can be recommended to include additional competencies of a certain type based on comparative measures) | [optional] 
**object_type** | **str** | If &#x60;score&#x60;, this object simply rates the matching uuid identified object. If &#x60;recommendation&#x60; an actual recommendation, with &#x60;recommendedContent&#x60; and other justifications, are provided. | [optional] 
**statistic_type** | **str** |  | [optional] 
**extra_info** | [**MetricsExtraInfo**](MetricsExtraInfo.md) |  | [optional] 
**metric_class** | **str** | In a scoring context (e.g. &#x60;objectType: score&#x60;) this describes what kind of framework is being recommended. In a recommendation context this describes the nature of the &#x60;recommendedContent&#x60; and the area that recommendation seeks to help the user improve in. For example, a &#x60;metricClass: actionable&#x60;, with &#x60;recommendedContent: Consider using more action verbs to describe this competency. 55 out of 100 users in your collaborative have done so.&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


