package COEN;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static ArrayList<Submission> subArray = new ArrayList<Submission>();
    public static ArrayList<Bucket> bucketArray = new ArrayList<Bucket>();
    public static ArrayList<Subscription> subscriptionArray = new ArrayList<Subscription>();
    public static ArrayList<User> userArray = new ArrayList<User>();

    public static void initsubArray() {
        int[] user_ids = {1, 5, 7};
        String[] titles = {"Google", "Stackoverflow", "Facebook"};
        String[] links = {"http://www.google.com", "http://www/stackoverflow.com", "http://www.facebook.com"};
        int[] ids = {1, 3, 8};
        String[] bucket_names = {"Search", "Programming", "Social"};
        int[] bucket_ids = {2, 5, 9};

        for (int i = 0; i < 3; i++) {
            Submission init_s = new Submission();
            init_s.setUser_id(user_ids[i]);
            init_s.setTitle(titles[i]);
            init_s.setLink(links[i]);
            init_s.setId(ids[i]);
            init_s.setBucket_name(bucket_names[i]);
            init_s.setBucket_id(bucket_ids[i]);

            subArray.add(init_s);
        }
    }

    public static void initbucketArray() {
        String[] bucket_names = {"Search", "Programming", "Social"};
        int[] bucket_ids = {2, 5, 9};

        for (int i = 0; i < 3; i++) {
            Bucket init_b = new Bucket();
            init_b.setName(bucket_names[i]);
            init_b.setId(bucket_ids[i]);
            init_b.setSubscribers(0);

            bucketArray.add(init_b);
        }
    }

    public static void inituserArray() {
        int[] user_ids = {1, 5, 7};
        String[] names = {"XinPing", "Obama", "Putin"};
        String[] u_names = {"xing", "obamama", "king"};

        for (int i = 0; i < 3; i++) {
            User init_u = new User();
            init_u.setId(user_ids[i]);
            init_u.setName(names[i]);
            init_u.setUsername(u_names[i]);

            userArray.add(init_u);
        }
    }

    public static void initsubscriptionArray() {
        int[] user_ids = {1, 5, 7};
        int[] bucket_ids = {2, 5, 9};

        for (int i = 0; i < 3; i++) {
            Subscription init_sub = new Subscription();
            init_sub.setUser_id(user_ids[i]);
            init_sub.setBucket_id(bucket_ids[i]);
            int tmp = i;
            Bucket bl = bucketArray.stream().filter(b -> (b.getId() == bucket_ids[tmp])).reduce((a, b) -> {
                throw new IllegalStateException("Multiple elements: " + a + ", " + b);
            }).get();

            bl.setSubscribers(bl.getSubscribers() + 1);

            subscriptionArray.add(init_sub);
        }

    }


    public static void main(String[] args) {

        initsubArray();
        initbucketArray();
        inituserArray();
        initsubscriptionArray();

        Scanner input = new Scanner(System.in);
        String choice;

        System.out.println("========================================");
        System.out.println("*                  Reddit              *");
        System.out.println("========================================");
        System.out.println("* S. Add Submission                    ");
        System.out.println("* F. Find Submission by ID             ");
        System.out.println("* D. Delete Submission by ID           ");
        System.out.println("* A. Display ALl Submissions		   ");
        System.out.println("* R. Get All Bucket Names			   ");
        System.out.println("* UP. Upvote a Submission by ID        ");
        System.out.println("* DW. Downvote a Submission by ID      ");
        System.out.println("* BS. Create a Bucket			       ");
        System.out.println("* LB. List all Available Bucket		   ");
        System.out.println("* SB. Subscribe to Bucket			   ");
        System.out.println("* U.  Add User To System			   ");
        System.out.println("* DU. Display All Users of System      ");
        System.out.println("* B.  Get all Submissions from Bucket  ");
        System.out.println("* DS. Display All Subscriptions  	   ");
        System.out.println("* Q. Quit Program                      ");
        System.out.println("========================================");
        System.out.println("");

        System.out.println("Choose one of the options from above. (E.g: Type 'A' to view all the submissions)");

        do {
            System.out.println();
            System.out.print("Choice : ");
            choice = input.next();
            String selection = choice.toLowerCase();

            switch (selection) {

                case "s":
                    Submission.store();
                    break;

                case "u":
                    User.store();
                    break;

                case "du":
                    User.show();
                    break;

                case "ds":
                    Subscription.show();
                    break;

                case "sb":
                    Subscription.subscribeToggle();
                    break;

                case "bs":
                    Bucket.store();
                    break;

                case "lb":
                    Bucket.show();
                    break;

                case "f":
                    Scanner ss = new Scanner(System.in);
                    System.out.println("Enter Id to Find Submission: ");
                    int f_id = ss.nextInt();
                    Submission s = Submission.get(f_id);
                    if (s != null) {
                        System.out.println(s.toString());
                    } else {
                        System.out.println("Submission doesn't exists. Create one first.");
                    }
                    break;

                case "d":
                    Scanner d_ss = new Scanner(System.in);
                    System.out.println("Enter ID to Delete Submission");
                    int d_id = d_ss.nextInt();
                    Submission.destroy(d_id);
                    break;

                case "a":
                    System.out.println("This is all We Got");
                    Submission.show();
                    break;

                case "b":
                    System.out.println("Enter Bucket Name to get all Submissions from that Bucket");
                    Scanner b_ss = new Scanner(System.in);
                    String b_id = b_ss.next();
                    Bucket.getSubmissions(b_id);
                    break;

                case "r":
                    System.out.println("Getting All Bucket Names for You");
                    Bucket.getBuckets();
                    break;

                case "up":
                    System.out.println("Enter Id to be Upvoted");
                    Scanner u_ss = new Scanner(System.in);
                    int u_id = u_ss.nextInt();
                    Vote.upVote(u_id);
                    break;

                case "dw":
                    System.out.println("Enter Id to be Upvoted");
                    Scanner dw_ss = new Scanner(System.in);
                    int dw_id = dw_ss.nextInt();
                    Vote.downVote(dw_id);
                    break;

                case "q":
                    System.out.println("Thanks");
                    break;

                default:
                    System.out.println("Invalid input! Please Enter one of these letters: V,A,E,D,F,S,L,O,Q");

            }
        } while (!(choice.equalsIgnoreCase("q")));

    }

}