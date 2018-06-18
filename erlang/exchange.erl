-module(exchange).
-export([master/0,master_thread/0,sleep_random/0]).

sleep_random() ->
    timer:sleep(round(timer:seconds(random:uniform()))).

master() ->
    {_, Tuples} = file:consult("calls.txt"),
    io:format("** Calls to be made **~n"),
    lists:map(fun (Pair) -> {S,R} = Pair, io:format("~p: ~p~n", [S,R]) end, Tuples),
    io:format("~n"),
    register(list_to_atom("master"),spawn(exchange,master_thread,[])),
    lists:map(fun (Pair) -> {S,_} = Pair, register(S,spawn(calling,friend_thread,[])) end, Tuples),
    lists:map(fun (Pair) -> master ! {Pair} end, Tuples),
    timer:sleep(1).

master_thread() ->
    receive
        {Tuples} ->
            {Sender,Receiver} = Tuples,
            Sender ! {Sender,Receiver},
            master_thread();
        {Sender,Receiver,Timestamp,Intro} ->
            io:format("~p received ~s message from ~p [~p]~n",[Receiver,Intro,Sender,Timestamp]),
            master_thread();
        {Sender,Receiver,Timestamp,Reply,Reply} ->
            io:format("~p received ~s message from ~p [~p]~n",[Sender,Reply,Receiver,Timestamp]),
            master_thread()
    after
        1500 ->
            {_, Pairs} = file:consult("calls.txt"),
            lists:map(fun(X) -> {S,_} = X, S ! kill, sleep_random() end, Pairs),
            timer:sleep(100),            
            io:format("~nMaster has received no replies for 1.5 seconds, ending...~n"),
            exit(kill)
    end.
