# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


__all__ = (
    "AccessReasonEnum",
    "AccessRoleEnum",
    "AccountBudgetProposalStatusEnum",
    "AccountBudgetProposalTypeEnum",
    "AccountBudgetStatusEnum",
    "AccountLinkStatusEnum",
    "AdCustomizerPlaceholderFieldEnum",
    "AdGroupAdRotationModeEnum",
    "AdGroupAdStatusEnum",
    "AdGroupCriterionApprovalStatusEnum",
    "AdGroupCriterionStatusEnum",
    "AdGroupStatusEnum",
    "AdGroupTypeEnum",
    "AdNetworkTypeEnum",
    "AdServingOptimizationStatusEnum",
    "AdStrengthEnum",
    "AdTypeEnum",
    "AdvertisingChannelSubTypeEnum",
    "AdvertisingChannelTypeEnum",
    "AffiliateLocationFeedRelationshipTypeEnum",
    "AffiliateLocationPlaceholderFieldEnum",
    "AgeRangeTypeEnum",
    "AppCampaignAppStoreEnum",
    "AppCampaignBiddingStrategyGoalTypeEnum",
    "AppPaymentModelTypeEnum",
    "AppPlaceholderFieldEnum",
    "AppStoreEnum",
    "AppUrlOperatingSystemTypeEnum",
    "AssetFieldTypeEnum",
    "AssetPerformanceLabelEnum",
    "AssetTypeEnum",
    "AttributionModelEnum",
    "BatchJobStatusEnum",
    "BidModifierSourceEnum",
    "BiddingSourceEnum",
    "BiddingStrategyStatusEnum",
    "BiddingStrategyTypeEnum",
    "BillingSetupStatusEnum",
    "BrandSafetySuitabilityEnum",
    "BudgetDeliveryMethodEnum",
    "BudgetPeriodEnum",
    "BudgetStatusEnum",
    "BudgetTypeEnum",
    "CallConversionReportingStateEnum",
    "CallPlaceholderFieldEnum",
    "CalloutPlaceholderFieldEnum",
    "CampaignCriterionStatusEnum",
    "CampaignDraftStatusEnum",
    "CampaignExperimentStatusEnum",
    "CampaignExperimentTrafficSplitTypeEnum",
    "CampaignExperimentTypeEnum",
    "CampaignServingStatusEnum",
    "CampaignSharedSetStatusEnum",
    "CampaignStatusEnum",
    "ChangeStatusOperationEnum",
    "ChangeStatusResourceTypeEnum",
    "ClickTypeEnum",
    "ContentLabelTypeEnum",
    "ConversionActionCategoryEnum",
    "ConversionActionCountingTypeEnum",
    "ConversionActionStatusEnum",
    "ConversionActionTypeEnum",
    "ConversionAdjustmentTypeEnum",
    "ConversionAttributionEventTypeEnum",
    "ConversionLagBucketEnum",
    "ConversionOrAdjustmentLagBucketEnum",
    "CriterionCategoryChannelAvailabilityModeEnum",
    "CriterionCategoryLocaleAvailabilityModeEnum",
    "CriterionSystemServingStatusEnum",
    "CriterionTypeEnum",
    "CustomInterestMemberTypeEnum",
    "CustomInterestStatusEnum",
    "CustomInterestTypeEnum",
    "CustomPlaceholderFieldEnum",
    "CustomerMatchUploadKeyTypeEnum",
    "CustomerPayPerConversionEligibilityFailureReasonEnum",
    "DataDrivenModelStatusEnum",
    "DayOfWeekEnum",
    "DeviceEnum",
    "DisplayAdFormatSettingEnum",
    "DisplayUploadProductTypeEnum",
    "DistanceBucketEnum",
    "DsaPageFeedCriterionFieldEnum",
    "EducationPlaceholderFieldEnum",
    "ExtensionSettingDeviceEnum",
    "ExtensionTypeEnum",
    "ExternalConversionSourceEnum",
    "FeedAttributeTypeEnum",
    "FeedItemQualityApprovalStatusEnum",
    "FeedItemQualityDisapprovalReasonEnum",
    "FeedItemStatusEnum",
    "FeedItemTargetDeviceEnum",
    "FeedItemTargetStatusEnum",
    "FeedItemTargetTypeEnum",
    "FeedItemValidationStatusEnum",
    "FeedLinkStatusEnum",
    "FeedMappingCriterionTypeEnum",
    "FeedMappingStatusEnum",
    "FeedOriginEnum",
    "FeedStatusEnum",
    "FlightPlaceholderFieldEnum",
    "FrequencyCapEventTypeEnum",
    "FrequencyCapLevelEnum",
    "FrequencyCapTimeUnitEnum",
    "GenderTypeEnum",
    "GeoTargetConstantStatusEnum",
    "GeoTargetingRestrictionEnum",
    "GeoTargetingTypeEnum",
    "GoogleAdsFieldCategoryEnum",
    "GoogleAdsFieldDataTypeEnum",
    "HotelDateSelectionTypeEnum",
    "HotelPlaceholderFieldEnum",
    "HotelPriceBucketEnum",
    "HotelRateTypeEnum",
    "IncomeRangeTypeEnum",
    "InteractionEventTypeEnum",
    "InteractionTypeEnum",
    "InvoiceTypeEnum",
    "JobPlaceholderFieldEnum",
    "KeywordMatchTypeEnum",
    "KeywordPlanCompetitionLevelEnum",
    "KeywordPlanForecastIntervalEnum",
    "KeywordPlanNetworkEnum",
    "LabelStatusEnum",
    "LegacyAppInstallAdAppStoreEnum",
    "LinkedAccountTypeEnum",
    "ListingGroupTypeEnum",
    "LocalPlaceholderFieldEnum",
    "LocationExtensionTargetingCriterionFieldEnum",
    "LocationGroupRadiusUnitsEnum",
    "LocationPlaceholderFieldEnum",
    "LocationSourceTypeEnum",
    "ManagerLinkStatusEnum",
    "MatchingFunctionContextTypeEnum",
    "MatchingFunctionOperatorEnum",
    "MediaTypeEnum",
    "MerchantCenterLinkStatusEnum",
    "MessagePlaceholderFieldEnum",
    "MimeTypeEnum",
    "MinuteOfHourEnum",
    "MobileAppVendorEnum",
    "MobileDeviceTypeEnum",
    "MonthOfYearEnum",
    "NegativeGeoTargetTypeEnum",
    "OfflineUserDataJobFailureReasonEnum",
    "OfflineUserDataJobStatusEnum",
    "OfflineUserDataJobTypeEnum",
    "OperatingSystemVersionOperatorTypeEnum",
    "OptimizationGoalTypeEnum",
    "ParentalStatusTypeEnum",
    "PaymentModeEnum",
    "PlaceholderTypeEnum",
    "PlacementTypeEnum",
    "PolicyApprovalStatusEnum",
    "PolicyReviewStatusEnum",
    "PolicyTopicEntryTypeEnum",
    "PolicyTopicEvidenceDestinationMismatchUrlTypeEnum",
    "PolicyTopicEvidenceDestinationNotWorkingDeviceEnum",
    "PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum",
    "PositiveGeoTargetTypeEnum",
    "PreferredContentTypeEnum",
    "PriceExtensionPriceQualifierEnum",
    "PriceExtensionPriceUnitEnum",
    "PriceExtensionTypeEnum",
    "PricePlaceholderFieldEnum",
    "ProductBiddingCategoryLevelEnum",
    "ProductBiddingCategoryStatusEnum",
    "ProductChannelEnum",
    "ProductChannelExclusivityEnum",
    "ProductConditionEnum",
    "ProductCustomAttributeIndexEnum",
    "ProductTypeLevelEnum",
    "PromotionExtensionDiscountModifierEnum",
    "PromotionExtensionOccasionEnum",
    "PromotionPlaceholderFieldEnum",
    "ProximityRadiusUnitsEnum",
    "QualityScoreBucketEnum",
    "ReachPlanAdLengthEnum",
    "ReachPlanAgeRangeEnum",
    "ReachPlanNetworkEnum",
    "RealEstatePlaceholderFieldEnum",
    "RecommendationTypeEnum",
    "SearchEngineResultsPageTypeEnum",
    "SearchTermMatchTypeEnum",
    "SearchTermTargetingStatusEnum",
    "SharedSetStatusEnum",
    "SharedSetTypeEnum",
    "SimulationModificationMethodEnum",
    "SimulationTypeEnum",
    "SitelinkPlaceholderFieldEnum",
    "SlotEnum",
    "SpendingLimitTypeEnum",
    "StructuredSnippetPlaceholderFieldEnum",
    "SummaryRowSettingEnum",
    "SystemManagedResourceSourceEnum",
    "TargetCpaOptInRecommendationGoalEnum",
    "TargetImpressionShareLocationEnum",
    "TargetingDimensionEnum",
    "TimeTypeEnum",
    "TrackingCodePageFormatEnum",
    "TrackingCodeTypeEnum",
    "TravelPlaceholderFieldEnum",
    "UserInterestTaxonomyTypeEnum",
    "UserListAccessStatusEnum",
    "UserListClosingReasonEnum",
    "UserListCombinedRuleOperatorEnum",
    "UserListCrmDataSourceTypeEnum",
    "UserListDateRuleItemOperatorEnum",
    "UserListLogicalRuleOperatorEnum",
    "UserListMembershipStatusEnum",
    "UserListNumberRuleItemOperatorEnum",
    "UserListPrepopulationStatusEnum",
    "UserListRuleTypeEnum",
    "UserListSizeRangeEnum",
    "UserListStringRuleItemOperatorEnum",
    "UserListTypeEnum",
    "VanityPharmaDisplayUrlModeEnum",
    "VanityPharmaTextEnum",
    "WebpageConditionOperandEnum",
    "WebpageConditionOperatorEnum",
    "ServedAssetFieldTypeEnum",
)