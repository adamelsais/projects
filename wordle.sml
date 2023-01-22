
structure Wordle =
struct

open Data

datatype result =
    Right
  | Wrong

(* each string is a single capital letter *)
type word = string Seq.seq

(* each string is a single capital letter, paired with a result *)
type guess_result = (string * result) Seq.seq

(* Checks a guess against a "hidden" word 'answer' and returns the result.

   E.g. check(makeWord "STAND", makeWord "STAMP") =
        <("S",Right), ("T",Right), ("A",Right), ("M",Wrong), ("P",Wrong) >

   Assumes both words have the same length.
*)
fun check(answer : word, guess : word) : guess_result =
    Seq.map (fn (ans_let, guess_let) => (guess_let,
                                         case ans_let = guess_let of
                                             true => Right
                                           | false => Wrong),
             Seq.zip(answer, guess))

(* little helper to make it easy to try check:
   try running runCheck("STAND","STAMP") in SMLNJ
   and you should see the above list
*)
fun runCheck(ans : string, guess : string) : (string * result) list =
    Seq.tolist(check (makeWord ans, makeWord guess))

    (*
        possibilities = seq of words
        guess = (letter, correctness) seq
        returns --> seq of words
        *)
(* TASK *)
fun update(possibilities : word Seq.seq, guess : guess_result) : word Seq.seq =
            (* (string, result)--> "word" (string seq)
              where wg is word guessed
             *)
    let val wg = Seq.map( fn (s,r) => s, guess)

        fun helpfilter(w, g) = (* input: word (string seq); output: bool *)
            case w of
              [] => true (* remove that "word" if empty *)
            | x :: xs => (case g of
                            [] => true (* leave word in list*)
                          | (s,r) :: ys => (case r of
                                              Right => ( case String.compare(x,s) of
                                                              EQUAL => helpfilter(xs,ys)
                                                            | _ => false)
                                            | Wrong =>( case String.compare(x,s) of
                                                           EQUAL => false
                                                          | _ => true )
                                            )
                          )


    Seq.filter(fn(word) => let val w = Seq.tolist(w)
                               val g = Seq.tolist(guess) in
                                helpfilter(w,g), possibilities)
                                end




(* TASK *)
fun suggest(possibilities : word Seq.seq) : word =
    raise Fail "unimplemented"

fun won(guess : guess_result) : bool =
    Seq.mapreduce(fn (w,r) => case r of Right => true | Wrong => false,
                  true,
                  fn (x,y) => x andalso y,
                  guess)

fun play(answer : word, possibilities : word Seq.seq, shouldPrint : bool) : int =
    let
        val maybePrint = case shouldPrint of true => print | false => fn _ => ()

        val guess_word = suggest possibilities
        val () = maybePrint ("Guessing " ^ (String.concat (Seq.tolist guess_word)) ^ "\n")
        val checked = check(answer,guess_word)
    in
        case won checked of
            true => (maybePrint ("You guessed it!\n"); 1)
          | false => play(answer, update(possibilities, checked), shouldPrint) + 1
    end

fun showReal (r : real) = Real.fmt (StringCvt.FIX (SOME 2)) r

fun histogram () =
    let val total_games = 100 (* Seq.length words *)
        val hist = Dict.toSeq(ExtractCombine.extractcombine (Int.compare, fn w => Seq.singleton(play(w,words, false), 1), Int.+, Seq.take(total_games, words)))
        val ps = Seq.tabulate (fn i => let val (guess,count) = Seq.nth(i,hist)
                                       in
                                           (guess,count, Seq.mapreduce(fn (g,c) => c, 0, fn (x,y) => x + y, Seq.take(i+1, hist)))
                                       end, Seq.length hist)
    in
    (print "Number of Guesses (N)\t| Games won in N guesses\t| Percentage won in N guesses \t| Percentage won in <=N guesses \n";
     Seq.map(fn (guess,count,cummulative) =>
             print (Int.toString guess ^ "\t\t\t| " ^
                    Int.toString count ^ "\t\t\t\t| " ^
                    showReal (100.0 * real count/real total_games) ^ "\t\t\t\t| " ^
                    showReal (100.0 * real cummulative/real total_games) ^ "\n"),
             ps))
    end

end
