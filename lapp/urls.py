from django.urls import path

from lapp import views

urlpatterns=[
    path('',views.main,name='main'),
    path('user_sign_up', views.user_sign_up, name='user_sign_up'),
    path('register', views.register, name='register'),
    path('log', views.log, name='log'),

    #Admin
    path('adminHome', views.adminHome, name='adminHome'),
    path('add_and_manage_agent', views.add_and_manage_agent, name='add_and_manage_agent'),
    path('add_agent', views.add_agent, name='add_agent'),
    path('addAgent', views.addAgent, name='addAgent'),
    path('editAgent/<int:id>', views.editAgent, name='editAgent'),
    path('updateAgent', views.updateAgent, name='updateAgent'),
    path('block_unblock_agent', views.block_unblock_agent, name='block_unblock_agent'),
    path('send_reply/<int:id>', views.send_reply, name='send_reply'),
    path('sendReply', views.sendReply, name='sendReply'),
    path('view_comp_send_rep', views.view_comp_send_rep, name='view_comp_send_rep'),
    path('deleteAgent<int:id>', views.deleteAgent, name='deleteAgent'),
    path('view_user', views.view_user, name='view_user'),
    #Agent
    path('add_manage_policy', views.add_manage_policy, name='add_manage_policy'),
    path('add_policy', views.add_policy, name='add_policy'),
    path('addPolicy', views.addPolicy, name='addPolicy'),
    path('editPolicy/<int:id>', views.editPolicy, name='editPolicy'),
    path('updatePolicy', views.updatePolicy, name='updatePolicy'),
    path('delPolicy<int:id>', views.delPolicy, name='delPolicy'),
    path('agent_dashboard', views.agent_dashboard, name='agent_dashboard'),
    path('doubt_reply/<int:id>', views.doubt_reply, name='doubt_reply'),
    path('doubtReply', views.doubtReply, name='doubtReply'),
    path('view_doubt_snd_rep', views.view_doubt_snd_rep, name='view_doubt_snd_rep'),
    path('view_req_updt_stat', views.view_req_updt_stat, name='view_req_updt_stat'),
    path('approve/<int:id>', views.approve, name='approve'),
    path('reject/<int:id>', views.reject, name='reject'),
    path('blockAgent/<int:id>', views.blockAgent, name='blockAgent'),
    path('unblockAgent/<int:id>', views.unblockAgent, name='unblockAgent'),
    path('view_feed_rating', views.view_feed_rating, name='view_feed_rating'),
    path('add_manage_file', views.add_manage_file, name='add_manage_file'),
    path('addFiles', views.addFiles, name='addFiles'),
    path('add_files', views.add_files, name='add_files'),
    path('delFiles/<int:id>', views.delFiles, name='delFiles'),
    path('editFiles/<int:id>', views.editFiles, name='editFiles'),
    path('updateFile', views.updateFile, name='updateFile'),
    #User
    path('user_home', views.user_home, name='user_home'),
    path('send_comp_view_rep', views.send_comp_view_rep, name='send_comp_view_rep'),
    path('send_dbt_view_rep', views.send_dbt_view_rep, name='send_dbt_view_rep'),
    path('send_comp', views.send_comp, name='send_comp'),
    path('sendComp', views.sendComp, name='sendComp'),
    path('send_dbt', views.send_dbt, name='send_dbt'),
    path('sendDbt', views.sendDbt, name='sendDbt'),
    path('send_feed_rating', views.send_feed_rating, name='send_feed_rating'),
    path('sendFeedRating', views.sendFeedRating, name='sendFeedRating'),
    path('view_plcy_snd_req', views.view_plcy_snd_req, name='view_plcy_snd_req'),
    path('sendplcyreq/<int:id>', views.sendplcyreq, name='sendplcyreq'),
    path('view_req_stat', views.view_req_stat, name='view_req_stat'),
    path('logout_view/', views.logout_view, name='logout_view'),

]