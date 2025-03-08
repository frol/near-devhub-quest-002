import near
from near_sdk_py import view, call, init, Context, Storage, Log, Balance, ONE_NEAR
import random

QUEST_AMOUNT = Balance(50 * ONE_NEAR)
WITHDRAW_DEPOSIT = Balance(0.1 * ONE_NEAR)

class QuestContract:
    @init
    def new(self):
        """Initialize the quest contract"""
        # TODO(near-sdk-py): implement such guard as part of @init decorator
        if Storage.has("activation_time"):
            near.panic_utf8("Quest contract already initialized")

        deployment_time = Context.block_timestamp()
        Log.info(f"Deployment time: {deployment_time}")
        # TODO(near-sdk-py): Consider automatically seeding the random number generator for every function call
        activation_time = deployment_time + (5 * 60 * 1000000000)

        Storage.set_json("activation_time", activation_time)
        Log.info(f"Quest contract initialized. Activation time: {activation_time}")
        # Oops, did I forget f"" string? No problem, I can view the activation time later

    # I wish I implemented it
    #
    # @view
    # def get_activation_time(self):
    #     """Get the activation timestamp of the quest"""
    #     return Storage.get_json("activation_time")

    @call
    def withdraw(self):
        """Withdraw the quest amount if called by the owner"""
        if Context.attached_deposit() < WITHDRAW_DEPOSIT:
            near.panic_utf8("Insufficient deposit for withdrawal")
        activation_time = Storage.get_json("activation_time")
        if Context.block_timestamp() < activation_time:
            near.panic_utf8("The quest is not active yet")

        current_balance = near.account_balance()
        if current_balance < QUEST_AMOUNT:
            near.panic_utf8("The quest is over. No more funds available.")

        promise = near.promise_batch_create(Context.signer_account_id())
        near.promise_batch_action_transfer(promise, QUEST_AMOUNT)

# Export the contract methods
contract = QuestContract()

# These exports make functions available to the NEAR runtime
new = contract.new
# get_activation_time = contract.get_activation_time
withdraw = contract.withdraw
