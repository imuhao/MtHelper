

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
      index_purchase_turnover =4 #订单金额
      index_estimated_revenue=5 #预计收入
      index_purchase_cost =6 #采购成本
      index_purchase_profit = 7 #采购利润
      index_profit_margin = 8 #利润率



      #订单数据
      index_order_view = 0 #订单号 
      index_order_goods_name = 1 #商品名称
      index_order_create_time = 2 #订单创建时间  
      index_order_status = 3 #订单状态 
      index_order_goods_count = 4 #下单数量  medicinePricetItem
      index_order_goods_price = 5 #购买单价
      index_order_total_price = 6 #下单总金额
      index_order_recipient_name = 7 #收货人
      index_order_recipient_phone = 8 #收货电话
      index_order_recipient_address = 9 #收货地址
      index_order_recipient_source = 10 #下单渠道  
      index_order_brushing = 11 #是否刷单
