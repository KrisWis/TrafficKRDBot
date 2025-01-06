from utils import userTexts
from typing import TypedDict, Dict

class PriceListItem(TypedDict):
    name: str
    text: str

price_list_texts: Dict[str, PriceListItem] = {
    "socials_develop": {"name": "📱 Развитие социальных сетей", "text": userTexts.socials_develop_text}, 
    "fresh_marketing": {"name": "📊 Свежий маркетинг", "text": userTexts.fresh_marketing_text}, 
    "good_websites": {"name": "🌐 Продающие сайты", "text": userTexts.good_websites_text}, 
    "flex_bots": {"name": "🤖 Гибкие боты", "text": userTexts.flex_bots_text}, 
    "design_and_creative": {"name": "🎨 Дизайн и креативы", "text": userTexts.design_and_creative_text}, 
    "billboards_and_banners": {"name": "🖼 Билборды и баннеры", "text": userTexts.billboards_and_banners_text}, 
    "traffic_tide": {"name": "👥 Прилив трафика", "text": userTexts.traffic_tide_text}, 
    "analytics_and_campaign": {"name": "📈 Аналитика и кампании", "text": userTexts.analytics_and_campaign_text}, 
    "meetings_and_shoots": {"name": "📹 Встречи и съёмки", "text": userTexts.meetings_and_shoots_text}, 
    "studying_and_personnel": {"name": "📚 Обучение и персонал", "text": userTexts.studying_and_personnel_text}, 
}