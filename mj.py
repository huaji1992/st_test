FROM novicezk/midjourney-proxy:1.3

ENV mj.discord.guild-id 1104787197980319916
ENV mj.discord.channel-id 1104787197980319919
ENV mj.discord.user-token MTA3NTExMjg2NTQ4NjM0NDI0Mg.G2OvuV.vB_A5WHj9B9kd01iwc63iWyfQZx-8TSaW-AmMM
ENV mj.discord.bot-token MTEwNTQ1MDM1MTI4MjM3Njc2NA.GA5RHw.bQF3HAKVc4PaQi5fYiOgS8FGfxj9LmkE3m3DxY

EXPOSE 8080

CMD ["midjourney-proxy"]
