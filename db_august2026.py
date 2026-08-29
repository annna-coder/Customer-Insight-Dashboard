import plotly.express as px
import pandas as pd
import streamlit as st


# """            (MAIN DAShBOARD)           """

st.set_page_config(page_title = 'The Dashboard', page_icon = ':bar-chart:', layout = 'wide', initial_sidebar_state = 'collapsed' )
df = pd.read_excel("Delinquency_prediction_dataset(ForProject).xlsx").fillna(0)

#st.header >.no color

#  --- (Header & Divider) ---
st.markdown(
    """
    <div style='text-align: left;'>
        <h1 style='color: #2C3E50; margin-bottom: 0;'>📊 Customer Insight Dashboard</h1>
        <p style='color: #7F8C8D; font-size: 16px; margin-top: 10px; margin-bottom: 10px;'>
            Overview of key metrics, demographics, financial health and risks.
        </p>
        <hr style='border: 1px solid #D5D8DC; margin-top: 0px; margin-bottom: 30px;'>
    </div>
    """,
    unsafe_allow_html=True
)
# """      (SIDEBAR)       """  

st.sidebar.header("Please Filter Here")

myselect_loc= st.sidebar.multiselect(
    "Select Location:",
    options= df["Location"].unique(),
    default= df["Location"].unique()[:3]
)

myselect_emp= st.sidebar.multiselect(
    "Select Employment:",
    options=df["Employment_Status"].unique(),
    default=df["Employment_Status"].unique()[:3]
)

myselect_cardType=st.sidebar.multiselect(
    "Select Credit-Card Type:",
    options=df["Credit_Card_Type"].unique(),
    default=df["Credit_Card_Type"].unique()[:3]
)

if not myselect_loc: 
    myselect_loc = df["Location"].unique()
    
if not myselect_emp:
    myselect_emp = df["Employment_Status"].unique()

if not myselect_cardType:
    myselect_cardType = df["Credit_Card_Type"].unique()

df_select= df.query("Location==@myselect_loc and Employment_Status==@myselect_emp and Credit_Card_Type ==@myselect_cardType")

# """          ___ KPI ___ (Bottom Lines)   """

total_customers = df['Customer_ID'].nunique()
avg_loan_balance = df['Loan_Balance'].mean()
avg_credit_score = df['Credit_Score'].mean()

avg_income = df['Income'].mean()
avg_missed_payments = df['Missed_Payments'].mean()
total_delinquent = df['Delinquent_Account'].sum()
delinquency_rate = (total_delinquent / total_customers) * 100


col1, col2, col3 = st.columns(3)
# -- Total Customers --

with col1:
    st.markdown(f"""
        <div style="background-color: #FFFFFF; border-left: 5px solid #CBD5E1; padding: 15px; border-radius: 5px; box-shadow: 2px 2px 5px grey; height: 130px;">
            <p style="color: grey; margin: 0; font-size: 14px;">Total Customers</p>
            <h2 style="margin: 0; color: #2C3E50; white-space: nowrap;">{total_customers}</h2>
        </div>
    """, unsafe_allow_html=True)

# -- Average Loan Balance --
#  (ကျန် ၄ ခုကိုလည်း အလားတူ ပြင်ပါ)
with col2:
    st.markdown(f"""
        <div style="background-color: #FFFFFF; border-left: 5px solid #CBD5E1; padding: 15px; border-radius: 5px; box-shadow: 2px 2px 5px grey; height: 130px;">
            <p style="color: grey; margin: 0; font-size: 14px;">Average Loan Balance</p>
            <h2 style="margin: 0; color: #2C3E50; white-space: nowrap;">${avg_loan_balance:,.0f}</h2>
        </div>
    """, unsafe_allow_html=True)

# -- Average Credit Score --
with col3:
    st.markdown(f"""
        <div style="background-color: #FFFFFF; border-left: 5px solid #CBD5E1; padding: 15px; border-radius: 5px; box-shadow: 2px 2px 5px grey; height: 130px;">
            <p style="color: grey; margin: 0; font-size: 14px;">Average Credit Score</p>
            <h2 style="margin: 0; color: #2C3E50; white-space: nowrap;">{avg_credit_score:,.0f}</h2>
        </div>
    """, unsafe_allow_html=True)


# အပေါ်က ကတ် (၃) ခုနဲ့ ကပ်မနေအောင် နေရာလွတ် (Space) နည်းနည်း ခြားပါမည်

st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

# Delinquency Rate ကတ်အတွက် ပြင်ဆင်ထားသော ပုံစံ
with col4:
    st.markdown(f"""
        <div style="background-color: #FFFFFF; border-left: 5px solid #EF4444; padding: 15px; border-radius: 5px; box-shadow: 2px 2px 5px grey; height: 130px;">
            <p style="color: grey; margin: 0; font-size: 14px;">Delinquency Rate</p>
            <h2 style="margin: 0; color: #2C3E50; white-space: nowrap;">{delinquency_rate:.1f}%</h2>
        </div>
    """, unsafe_allow_html=True)

# (Average Income)
with col5:
    st.markdown(f"""
        <div style="background-color: #FFFFFF; border-left: 5px solid #CBD5E1; padding: 15px; border-radius: 5px; box-shadow: 2px 2px 5px grey; height: 130px;">
            <p style="color: grey; margin: 0; font-size: 14px;">Average Income</p>
            <h2 style="margin: 0; color: #2C3E50; white-space: nowrap;">${avg_income:,.0f}</h2>
        </div>
    """, unsafe_allow_html=True)




# (Average Missed Payments)
with col6:
    st.markdown(f"""
        <div style="background-color: #FFFFFF; border-left: 5px solid #CBD5E1; padding: 15px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); height: 130px;">
            <p style="color: #64748B; margin: 0; font-size: 14px;">Average Missed Payments</p>
            <h2 style="margin: 0; color: #2C3E50; white-space: nowrap; display: flex; align-items: baseline;">
                {avg_missed_payments:.1f} <span style="font-size: 15px; color: #94A3B8; margin-left: 1px; font-weight: 500;">times</span>
            </h2>
        </div>
    """, unsafe_allow_html=True)


# KPI ကတ် (၆) ခု ပြီးသွားတဲ့ နေရာအောက်တွင် အောက်ပါ Code လေး ထည့်ပေးပါ
st.markdown("<br><br>", unsafe_allow_html=True) # <br> တစ်ခုက တစ်ကြောင်းစာ (Space) ခြားပေးသည်

# ကဏ္ဍများကို Tabs များဖြင့် သီးသန့် ခွဲခြားခြင်း
tab_loc_emp, tab_card = st.tabs(["Location & Employment", "Card Type Analysis"])

with tab_loc_emp:
    col1, col2 = st.columns(2) 
    
    with col1:
        st.markdown("#### Customers by Location")
        st.markdown("<p style='color:#7F8C8D; font-size:12px;'>Customer distribution across different cities.</p>", unsafe_allow_html=True)
        
        # Location Bar Chart
        cus_by_loc = df_select.groupby("Location")["Customer_ID"].size().reset_index(name="Count")
        max_count = cus_by_loc["Count"].max()
        cus_by_loc["Highlight"] = cus_by_loc["Count"].apply(lambda x: "Highest" if x == max_count else "Normal")
        
        fig_loc = px.bar(
            cus_by_loc, 
            x="Location", 
            y="Count", 
            color="Highlight", 
            color_discrete_map={
                "Highest": "#3975A9", 
                "Normal": "#CBD5E1"   
            },
            labels={"Location": "- City -"} 
        )
        fig_loc.update_layout(
            xaxis_title="", 
            yaxis_title="number of customers", 
            xaxis_tickangle= 0, 
            showlegend=False, 
            margin= dict(t=20, b= 20) 
        )
        st.plotly_chart(fig_loc, use_container_width=True)

    with col2:
        st.markdown("#### Employment Breakdown")
        st.markdown("<p style='color:#7F8C8D; font-size:12px;'>Proportion of customers by employment status.</p>", unsafe_allow_html=True)
        
        # Employment Donut Chart
        cus_by_emp = df_select.groupby("Employment_Status")["Customer_ID"].size().reset_index(name="Count")
        premium_muted_palette = [
            "#6B8EA5", "#CFA073", "#4F5965", "#8D9AA6", "#DEE3E9", "#A39B9E" 
        ]
        
        fig_emp = px.pie(
            cus_by_emp, 
            names="Employment_Status", 
            values="Count", 
            hole=0.4, 
            color_discrete_sequence=premium_muted_palette 
        )
        st.plotly_chart(fig_emp, use_container_width=True)

with tab_card:
    st.markdown("#### Customers by Card Type")
    st.markdown("<p style='color:#7F8C8D; font-size:12px;'>Larger bubbles indicate higher adoption rates among customer segments.</p>", unsafe_allow_html=True)
    
    # Card Type Bubble Chart
    cus_by_card = df_select.groupby("Credit_Card_Type")["Customer_ID"].size().reset_index(name="Count")
    fig_card = px.scatter(
        cus_by_card,
        x="Credit_Card_Type",
        y="Count",
        size="Count",          
        color="Credit_Card_Type", 
        color_discrete_map={
            "Platinum": "#0F172A",
            "Gold": "#BF813B",
            "Business": "#2B5B84",
            "Standard": "#64748B",
            "Student": "#CBD5E1"
        },
        text="Credit_Card_Type", 
        size_max=60,
        labels={"Credit_Card_Type": "Card Type"}       
    )
    max_y_value = cus_by_card["Count"].max()
    y_upper_limit = max_y_value + (max_y_value * 0.35)
    
    fig_card.update_traces(textposition='top center', cliponaxis=False)
    fig_card.update_layout(
        xaxis_title="", 
        yaxis_title="number of customers",
        yaxis_range=[0, y_upper_limit],
        showlegend=False
    )
    st.plotly_chart(fig_card, use_container_width=True)

# ကဏ္ဍများကို Tabs များဖြင့် ခွဲခြားခြင်း
tab1, tab2, tab3 = st.tabs(["Credit Score & Income", "Credit Utilization","Credit Score & DTI Analysis"])
with tab1:
    st.markdown("### Credit Score & Income Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # ၁။ Credit Score Distribution
        fig_credit_score = px.histogram(
            df_select, 
            x="Credit_Score", 
            nbins=50, 
            color_discrete_sequence=["#65798E"], 
            title="<b>Credit Score Distribution</b>"
        )
        fig_credit_score.update_layout(
            xaxis_title="Credit Score", 
            yaxis_title="number of customers"
        )
        st.plotly_chart(fig_credit_score, use_container_width=True)

    with col2:
        # ၂။ Credit Score vs Income
        fig_cd_score_income = px.scatter(
            df_select,
            x="Credit_Score", 
            y="Income", 
            color="Employment_Status", 
            color_discrete_sequence=px.colors.qualitative.Prism, 
            title="<b>Credit Score vs Income</b>"
        )
        fig_cd_score_income.update_layout(
            xaxis_title="Credit Score"
        )
        st.plotly_chart(fig_cd_score_income, use_container_width=True)

with tab2:
    st.markdown("### Credit Utilization & Risk")
    st.markdown("<p style='color:#7F8C8D; font-size:12px;'>Credit Utilization Distribution</p>", unsafe_allow_html=True)
    # ၃။ Credit Utilization
    fig_credit_util = px.box(
        df_select,
        x="Credit_Utilization", 
        color_discrete_sequence=['#E74C3C'],
        hover_data=["Customer_ID", "Employment_Status"]
    )
    
    # နေရာလွတ်များကို ဖြတ်တောက်ရန် အမြင့်နှင့် Margin ကို ပြင်ဆင်ခြင်း
    fig_credit_util.update_layout(
        height=250, 
        margin=dict(t=40, b=0, l=0, r=0)
    )
    st.plotly_chart(fig_credit_util, use_container_width=True)

    # 0.85 ထက်ကျော်လွန်ပြီး အကြွေးသုံးထားသူများ
    outliers = df_select[df_select["Credit_Utilization"] > 0.85]

    # ခေါင်းစဉ်ကို သပ်ရပ်အောင် ပြင်ဆင်ခြင်း
    st.markdown("<div style='color: #E74C3C; font-weight: 600; font-size: 16px; margin-bottom: 10px;'>High Risk Customers (Utilization > 85%)</div>", unsafe_allow_html=True)
    
    st.dataframe(
        outliers[["Customer_ID", "Income", "Credit_Utilization", "Credit_Card_Type"]], 
        use_container_width=True
    )
with tab3:
    # DTI ကို အုပ်စု (၄) စု ခွဲပါမည် (pd.cut အသုံးပြုခြင်း)
    st.markdown("### Credit Score vs DTI")
    st.markdown("<p style='color:#7F8C8D; font-size:12px;'>Credit Score spread across DTI Risk Groups.</p>", unsafe_allow_html=True)
        
    df_select["DTI_gp"] = pd.cut(
        df_select["Debt_to_Income_Ratio"],
        bins=[0, 0.20, 0.36, 0.43, float("inf")],
        labels=["Low Risk", "Moderate", "Elevated", "High Risk"]
    )

    # Risk အဆင့်အလိုက် အရောင်များ သတ်မှတ်ခြင်း (အကောင်းမှ အဆိုးသို့)
    risk_colors = ["#2ECC71", "#F1C40F", "#E67E22", "#E74C3C"] 

    # ခ) ခွဲထားသော အုပ်စုများအလိုက် Credit Score ကို Box Plot ဖြင့် နှိုင်းယှဉ်မည်
    fig_dti_gp_by_credit = px.box(
        df_select,
        x="DTI_gp",          
        y="Credit_Score",    
        color="DTI_gp",
        labels={"DTI_gp": "DTI Risk Group"},
        
        # ပြဿနာကို ဖြေရှင်းပေးမည့် အပိုင်း (အစီအစဉ် သတ်မှတ်ခြင်း)
        category_orders={"DTI_gp": ["Low Risk", "Moderate", "Elevated", "High Risk"]},
        color_discrete_sequence=risk_colors # အရောင်များကိုပါ အစဉ်လိုက် သုတ်ခြင်း
    )

    fig_dti_gp_by_credit.update_layout(
        xaxis_title="", 
        yaxis_title="credit scores",
    )

    st.plotly_chart(fig_dti_gp_by_credit, use_container_width=True)

tab1, tab2, tab3 = st.tabs(["Loan Balance by Location", "DTI by Employment", "On-time / Late / Missed %"])
with tab1:
    st.markdown("#####  Total Loan Balance by Location")
    
    # ၄။ Loan Balance by Location
    # ပထမဆုံး မြို့အလိုက် ချေးငွေ(Loan_Balance) တွေကို စုပေါင်း(sum) ပါမည်။
    loan_by_loc = df_select.groupby("Location")["Loan_Balance"].sum().reset_index()

    fig_loan_by_loc = px.bar(
        loan_by_loc,
        x="Location",
        y="Loan_Balance",
        color="Location",
        color_discrete_sequence= px.colors.qualitative.Prism
    )
    fig_loan_by_loc.update_layout(
        xaxis_title="", 
        yaxis_title="Loan Balance",
        xaxis_tickangle= 0,
        margin= dict(t=20, b= 20) 
    )
    st.plotly_chart(fig_loan_by_loc, use_container_width=True)
        
with tab2:
    st.markdown("#####  Average DTI by Employment  ")
    # ၅။ DTI by Employment (ပျမ်းမျှ DTI ကို ရှာပါမည်)
    dti_by_emp = df_select.groupby("Employment_Status")["Debt_to_Income_Ratio"].mean().reset_index()

    fig_dti_by_emp = px.bar(
        dti_by_emp,
        x="Employment_Status",
        y="Debt_to_Income_Ratio",
        color="Employment_Status",
        color_discrete_sequence= px.colors.qualitative.Bold,
        labels={"Employment_Status": "Employment Status"}
    )
    fig_dti_by_emp.update_layout(
                xaxis_title="", 
                yaxis_title="Debt to Income Ratio",
                xaxis_tickangle= 0,
                margin= dict(t=20, b= 20) 
            )
            
    st.plotly_chart(fig_dti_by_emp, use_container_width=True)

#"""fig = px.colors.qualitative.swatches()
#fig.show()"""
with tab3:
    st.markdown("##### 📅 Month 1-6 Payment Behavior")
    
    # ခေါင်းစဉ် (Title) နှင့် ဇယား (Chart) အကြား နေရာလွတ်ချန်ရန်
    #st.markdown("<br>", unsafe_allow_html=True)
    
    # (၁) ကော်လံ ၆ ခုကို အရည်ပျော်ချမည် (Melt)
    month_cols = ["Month_1", "Month_2", "Month_3", "Month_4", "Month_5", "Month_6"]
    melted_df = df_select.melt(id_vars="Customer_ID", value_vars=month_cols, var_name="Month", value_name="Status")

    # (၂) ရေတွက်ခြင်း
    result = melted_df.groupby(["Customer_ID", "Status"]).size().unstack(fill_value=0)

    # (၃) ရာခိုင်နှုန်း တွက်မည်
    result["total"] = result["Late"] + result["Missed"] + result["On-time"]
    result["Late%"] = result["Late"] / result["total"] * 100
    result["Missed%"] = result["Missed"] / result["total"] * 100
    result["On-time%"] = result["On-time"] / result["total"] * 100

    # Index ကိုဖြုတ်ပြီး Customer_ID ကို သာမန်ကော်လံအဖြစ် ပြန်ပြောင်းမည်
    result_df = result.reset_index()
    result_df.columns.name = None 

    # ဇယားကို ထပ်မံ Melt မည်
    plot_df = result_df.melt(
        id_vars="Customer_ID", 
        value_vars=["Late%", "Missed%", "On-time%"], 
        var_name="Payment_Type", 
        value_name="Percentage"
    )

    fig_behavior = px.box(
        plot_df,
        x="Payment_Type",
        y="Percentage",
        color="Payment_Type", 
        # ပြဿနာ (၁) ဖြေရှင်းချက် - Category ကို စိမ်း -> ဝါ -> နီ အတိုင်း အတိအကျ စီမည်
        category_orders={"Payment_Type": ["On-time%", "Late%", "Missed%"]}, 
        color_discrete_map={
            "On-time%": "#2ECC71", # အစိမ်း
            "Late%": "#F1C40F",    # အဝါ
            "Missed%": "#E74C3C"   # အနီ
        },
        title="<b>Customer Payment Behavior Distribution (%)</b>"
    )
    
    fig_behavior.update_layout(
        xaxis_title="", 
        yaxis_title="Percentage (%)",
        margin=dict(t=40) # Title နှင့် Chart အကြား အကွာအဝေးကို လျှော့ချရန် Top Margin ချိန်ညှိခြင်း
    )
    st.plotly_chart(fig_behavior, use_container_width=True)

    # ပြဿနာ (၂) ဖြေရှင်းချက် - Chart နှင့် Dataframe ကြား နေရာလွတ်အကျယ်ကြီး ချန်ပြီး မျဉ်းတားမည်
    #st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    #st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<b>⚠️ Action Required: High Risk Customers</b>", unsafe_allow_html=True)
    st.markdown("<p style='color:grey; font-size:12px;'>Customers sorted by highest Missed and Late payment percentages.</p>", unsafe_allow_html=True)

    # Missed% အများဆုံးလူကို အပေါ်ဆုံးရောက်အောင် (Descending) စီမည်။
    risk_table = result_df.sort_values(by=["Missed%", "Late%"], ascending=[False, False])
    risk_table_display = risk_table[["Customer_ID", "Missed%", "Late%", "On-time%"]]

    # မျက်နှာပြင်ပေါ်တွင် ဇယား (Dataframe) ဖော်ပြမည်
    st.dataframe(risk_table_display, use_container_width=True)



# ---------------------------------------------------------
# အခြေခံ Data ပုံစံပြောင်းခြင်း (Melt) - သင့်ဆီမှ df_select ကို တိုက်ရိုက်အသုံးပြုပါမည်
# ---------------------------------------------------------
month_cols = ["Month_1", "Month_2", "Month_3", "Month_4", "Month_5", "Month_6"]

# Location နှင့် Employment_Status တို့ကိုပါ id_vars အဖြစ် ထည့်သွင်းထားပါသည်
melted_df = df_select.melt(
    id_vars=["Customer_ID", "Location", "Employment_Status"], 
    value_vars=month_cols, 
    var_name="Month", 
    value_name="Status"
)

# "Missed" ဖြစ်သော အချက်အလက်များကိုသာ သီးသန့်စစ်ထုတ်ထားခြင်း (Tab 2 နှင့် 3 တွင် သုံးရန်)
missed_df = melted_df[melted_df["Status"] == "Missed"]

# ---------------------------------------------------------
# Tab (၄) ခု တည်ဆောက်ခြင်း (Emoji များ ဖယ်ရှားထားပါသည်)
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "Monthly Trend", 
    "Missed by Location", 
    "Missed by Employment", 
    "Customer Behavior"
])

# ==========================================
# TAB 1: Monthly Payment Trend
# ==========================================
with tab1:
    st.markdown("##### Monthly Payment Trend")
    st.markdown("<p style='color:grey; font-size:12px;'>Monthly trend of On-time, Late, and Missed payment statuses over the 6-month period.</p>", unsafe_allow_html=True)
    
    # လအလိုက် Status အရေအတွက်ကို ရေတွက်ခြင်း
    monthly_trend = melted_df.groupby(["Month", "Status"]).size().reset_index(name="Count")
    
    fig_trend = px.line(
        monthly_trend,
        x="Month",
        y="Count",
        color="Status",
        markers=True,
        title="<b>Overall Payment Trend Over 6 Months</b>",
        category_orders={"Month": month_cols, "Status": ["On-time", "Late", "Missed"]},
        color_discrete_map={
            "On-time": "#2ECC71", # အစိမ်း
            "Late": "#F1C40F",    # အဝါ
            "Missed": "#E74C3C"   # အနီ
        }
    )
    fig_trend.update_layout(xaxis_title="", yaxis_title="Number of Payments")
    st.plotly_chart(fig_trend, use_container_width=True)

# ==========================================
# TAB 2: Missed Payments by Location
# ==========================================
with tab2:
    st.markdown("##### Missed Payments by Location")
    st.markdown("<p style='color:grey; font-size:12px;'>Total Missed Payments by Region (Regions with the highest number of missed payments.)</p>", unsafe_allow_html=True)
    
    # မြို့အလိုက် ပျက်ကွက်မှုများကို ရေတွက်ခြင်း
    missed_loc = missed_df.groupby("Location").size().reset_index(name="Missed_Count")
    missed_loc = missed_loc.sort_values(by="Missed_Count", ascending=False) # အများဆုံးမှ အနည်းဆုံးသို့ စီခြင်း
    
    fig_loc = px.bar(
        missed_loc,
        x="Location",
        y="Missed_Count",
        color="Location",
        color_discrete_sequence=px.colors.qualitative.Antique
    )
    fig_loc.update_layout(xaxis_title="", yaxis_title="Total Missed Payments", showlegend=False)
    st.plotly_chart(fig_loc, use_container_width=True)

# ==========================================
# TAB 3: Missed Payments by Employment
# ==========================================
with tab3:
    st.markdown("##### Missed Payments Trend by Employment")
    st.markdown("<p style='color:grey; font-size:12px;'>Monthly growth of missed payments categorized by employment status.</p>", unsafe_allow_html=True)
    
    # အလုပ်အကိုင်နှင့် လအလိုက် ရေတွက်မည်
    missed_emp = missed_df.groupby(["Month", "Employment_Status"]).size().reset_index(name="Missed_Count")
    
    # Area Chart ဆွဲမည်
    fig_missed_emp = px.area(
        missed_emp,
        x="Month",
        y="Missed_Count",
        color="Employment_Status",
        markers=True,
        category_orders={"Month": month_cols},
        color_discrete_sequence=px.colors.qualitative.Prism
    )
    fig_missed_emp.update_layout(xaxis_title="", yaxis_title="Missed Count")
    st.plotly_chart(fig_missed_emp, use_container_width=True)

# ==========================================
# TAB 4: Payment Behavior by Customer
# ==========================================
with tab4:
    st.markdown("##### Customer Payment Behavior Detail")
    st.markdown("<p style='color:grey; font-size:12px;'>Individual customer payment behavior percentages (sorted by highest risk).</p>", unsafe_allow_html=True)
    
    # Customer တစ်ယောက်ချင်းစီအတွက် Status များကို ရေတွက်မည်
    result = melted_df.groupby(["Customer_ID", "Status"]).size().unstack(fill_value=0)
    
    # Data ထဲတွင် Late သို့မဟုတ် Missed လုံးဝမရှိသူများအတွက် Error မတက်စေရန် စစ်ဆေးခြင်း
    for col in ["Late", "Missed", "On-time"]:
        if col not in result.columns:
            result[col] = 0
            
    # ရာခိုင်နှုန်း တွက်မည်
    result["total"] = result["Late"] + result["Missed"] + result["On-time"]
    result["Late%"] = (result["Late"] / result["total"] * 100).round(1)
    result["Missed%"] = (result["Missed"] / result["total"] * 100).round(1)
    result["On-time%"] = (result["On-time"] / result["total"] * 100).round(1)
    
    # Index ကိုဖြုတ်ပြီး သာမန်ကော်လံအဖြစ် ပြန်ပြောင်းမည်
    result_df = result.reset_index()
    result_df.columns.name = None 
    
    # Missed% အများဆုံးလူကို အပေါ်ဆုံးရောက်အောင် စီမည်
    risk_table = result_df.sort_values(by=["Missed%", "Late%"], ascending=[False, False])
    
    # Table တွင် ပြသလိုသော ကော်လံများကိုသာ ရွေးထုတ်မည်
    risk_table_display = risk_table[["Customer_ID", "Missed%", "Late%", "On-time%"]]
    
    # မျက်နှာပြင်ပေါ်တွင် ဇယား (Dataframe) ဖော်ပြမည်
    st.dataframe(risk_table_display, use_container_width=True)


# ---------------------------------------------------------
# ၂။ Risk Scoring System တည်ဆောက်ခြင်း
# ---------------------------------------------------------
# အချိန်မီသွင်းပါက 0၊ နောက်ကျပါက 1၊ လုံးဝမသွင်းပါက 2 ဟု သတ်မှတ်မည်
score_map = {"On-time": 0, "Late": 1, "Missed": 2}
month_cols = ["Month_1", "Month_2", "Month_3", "Month_4", "Month_5", "Month_6"]

# Customer တစ်ယောက်ချင်းစီအတွက် လ ၆ လစာ အမှတ်ပေါင်း (Risk Score) တွက်ချက်ခြင်း
df["Risk_Score"] = df[month_cols].replace(score_map).sum(axis=1)

# အမှတ်ပေါ် မူတည်၍ Low/Medium/High Risk သတ်မှတ်မည့် Function
def get_risk_level(score):
    if score <= 2:
        return "Low Risk"
    elif score <= 5:
        return "Medium Risk"
    else:
        return "High Risk"

df["Risk_Level"] = df["Risk_Score"].apply(get_risk_level)

# ---------------------------------------------------------
# ၃။ Tab ၄ ခု တည်ဆောက်ခြင်း
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "Risk Overview", 
    "High Risk by Location", 
    "Risk by Demographics", 
    "Top High-Risk Customers"
])

# ==========================================
# TAB 1: Risk Overview (Low/Medium/High Risk ဖြန့်ကျက်မှု)
# ==========================================
with tab1:
    st.markdown("#### Risk Level Distribution")
    st.markdown("<p style='color:grey; font-size:12px;'>Proportion of customers categorized as Low, Medium, and High Risk. / Overall Risk Level Distribution </p>", unsafe_allow_html=True)
    
    df_risk_level = df["Risk_Level"].value_counts().reset_index()
    
    fig_risk_dist = px.pie(
        df_risk_level, 
        values="count", 
        names="Risk_Level",
        hole=0.4, 
        color="Risk_Level",
        color_discrete_map={
            "Low Risk": "#2ECC71", 
            "Medium Risk": "#F1C40F", 
            "High Risk": "#E74C3C"
        }
    )
    st.plotly_chart(fig_risk_dist, use_container_width=True)

# ==========================================
# TAB 2: High Risk by Location
# ==========================================
with tab2:
    st.markdown("#### High Risk Customers by Location")
    st.markdown("<p style='color:grey; font-size:12px;'>Geographical distribution of customers classified as High Risk.</p>", unsafe_allow_html=True)
    
    high_risk_loc = df[df["Risk_Level"] == "High Risk"].groupby("Location").size().reset_index(name="Count")
    high_risk_loc = high_risk_loc.sort_values(by="Count", ascending=True)
    
    fig_high_risk_loc = px.bar(
        high_risk_loc,
        x="Count",
        y="Location",
        orientation="h",
        title="High Risk Customers by Region",
        color_discrete_sequence=["#E74C3C"]
    )
    fig_high_risk_loc.update_layout(xaxis_title="Number of Customers", yaxis_title="Location")
    st.plotly_chart(fig_high_risk_loc, use_container_width=True)

# ==========================================
# TAB 3: Risk by Demographics (Employment & Card Type)
# ==========================================
with tab3:
    st.markdown("#### Risk Distribution by Demographics")
    st.markdown("<p style='color:grey; font-size:12px;'>Risk level breakdown across employment statuses and credit card types.</p>", unsafe_allow_html=True)
    
    # Treemap (Employment Status)
    risk_by_emp = df.groupby(["Employment_Status", "Risk_Level"]).size().reset_index(name="Count")
    fig_risk_emp = px.treemap(
        risk_by_emp,
        path=[px.Constant("All Employment"), "Employment_Status", "Risk_Level"],
        values="Count",
        color="Risk_Level",
        color_discrete_map={"Low Risk": "#2ECC71", "Medium Risk": "#F1C40F", "High Risk": "#E74C3C"},
        title="Risk Level by Employment Status"
    )
    st.plotly_chart(fig_risk_emp, use_container_width=True)
    
    # Treemap (Credit Card Type)
    risk_by_card = df.groupby(["Credit_Card_Type", "Risk_Level"]).size().reset_index(name="Count")
    fig_risk_card = px.treemap(
        risk_by_card,
        path=[px.Constant("All Cards"), "Credit_Card_Type", "Risk_Level"],
        values="Count",
        color="Risk_Level",
        color_discrete_map={"Low Risk": "#2ECC71", "Medium Risk": "#F1C40F", "High Risk": "#E74C3C"},
        title="Risk Level by Credit Card Type"
    )
    st.plotly_chart(fig_risk_card, use_container_width=True)

# ==========================================
# TAB 4: Top High-Risk Customers
# ==========================================
with tab4:
    st.markdown("#### Top 10 Highest Risk Customers")
    st.markdown("<p style='color:grey; font-size:12px;'>Detailed list of the top 10 customers with the highest delinquency risk scores.</p>", unsafe_allow_html=True)
    
    # အမှတ်အများဆုံး (အန္တရာယ်အများဆုံး) ၁၀ ဦးကို ရွေးထုတ်ခြင်း
    top_10_risk = df.sort_values(by="Risk_Score", ascending=False).head(10)
    top_10_display = top_10_risk[["Customer_ID", "Location", "Employment_Status", "Credit_Card_Type", "Risk_Score", "Risk_Level"]]
    
    st.dataframe(
        top_10_display.style.highlight_max(subset=["Risk_Score"], color="#F5B7B1"), 
        use_container_width=True
    )