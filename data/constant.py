

# dealAmountValue = dealAmount["amount"] #今日营业额
# dealRelativeCycle = dealAmount["relativeCycle"] #营业额环比
# dealRankingInterval = dealAmount["rankingInterval"] #排名

# transactionTurnover = transactionVolume["turnover"] #成交单量
# transactionRelativeCycle = transactionVolume["relativeCycle"] #单量环比

# averagePrice = singleAveragePrice["averagePrice"] #单均价

# refundAmountValue = refundAmount["amount"] #退款金额
# refundRelativeCycle = refundAmount["relativeCycle"] #退款金额环比


class Contants:

      #店铺数据
      index_name = 0 #店铺名称
      index_deal_amount_value = 1 #今日营业额
      index_deal_relative_cycle =2 #营业额环比
      index_deal_ranking_interval=3 #营业额排名
      index_transaction_turnover = 4 #成交单量
      index_transaction_relative_cycle =5#单量环比
      index_average_price = 6 #订单均价
      index_refund_amount_value = 7 #退款金额
      index_refund_relative_cycle = 8 #退款金额环比


      #采购数据
      index_purchase_shop_name = 0 #店铺名称
      index_purchase_order_number =1 #订单数
      index_purchase_add_time = 2 #采购时间
      index_purchase_order_time = 3 #订单时间
      index_purchase_turnover =4 #采购营业额
      index_purchase_cost =5 #采购成本
      index_purchase_profit = 6 #采购利润
      index_profit_margin = 7 #利润率