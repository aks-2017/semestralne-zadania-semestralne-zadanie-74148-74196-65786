from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
import requests

class L2Switch(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)

        print ("klobasa")
        print ("nova brancha 2")

        @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
        def _packet_in_handler(self, ev):
            msg = ev.msg
            #msg = ev.msg
            #dp = msg.datapath
            #ofp = dp.ofproto
            #ofp_parser = dp.ofproto_parser

            #actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
            #out = ofp_parser.OFPPacketOut(
            #    datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port,
            #    actions=actions)
            #dp.send_msg(out)

            print (msg)

            r = requests.get('http://localhost:8080/stats/switches')
            r.status_code

            # extracting data in json format
            data = r.json()

            print (data)


            print ("salama")