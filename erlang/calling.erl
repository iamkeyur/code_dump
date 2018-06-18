-module(calling).
-export([friend_thread/0,get_timestamp/0]).

get_timestamp() ->
    {_,_,Micro} = erlang:now(),
    Micro.

sleep_random() ->
    timer:sleep(round(timer:seconds(random:uniform()))).

friend_thread() ->
    receive
        {Sender,Receivers} ->
            Intro = "intro",
            lists:map(fun (Receiver) -> Timestamp = get_timestamp(),Receiver ! {Sender,Receiver,Timestamp,Intro} end, Receivers),
            friend_thread();
        {Sender,Receiver,Timestamp,I} ->
            Reply = "reply",
            sleep_random(),
            Receiver ! {Sender,Receiver,Timestamp,Reply,Reply},
            master ! {Sender,Receiver,Timestamp,I},
            friend_thread();
        {Sender,Receiver,Timestamp,Reply,Reply} ->
            sleep_random(),            
            master ! {Sender,Receiver,Timestamp,Reply,Reply},
            friend_thread();
        kill ->
            {_,N} = erlang:process_info(self(), registered_name),
            io:format("~nProcess ~p has received no calls for 1 second, ending...~n~n",[N]),
            exit(kill)
    end.
